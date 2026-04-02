#!/usr/bin/env python3
"""
Campaign mail-merge send script.

Reads segmented contact CSVs, fills email templates, sends via SMTP.
Logs every send with timestamp for tracking.

Usage:
    # Dry run (no emails sent, just preview):
    python campaign_send.py --dry-run --category 1_advocates

    # Send to advocates:
    python campaign_send.py --category 1_advocates

    # Send to all oversight bodies:
    python campaign_send.py --category 4_oversight

    # Send specific version:
    python campaign_send.py --category 4_oversight --version B

    # List available categories:
    python campaign_send.py --list

    # Preview a single email:
    python campaign_send.py --preview --to "info@hrlc.org.au"
"""

import argparse
import csv
import json
import os
import smtplib
import sys
import time
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration — EDIT THESE
# ---------------------------------------------------------------------------

SMTP_HOST = ""          # e.g. "smtp.gmail.com"
SMTP_PORT = 587         # TLS port
SMTP_USER = ""          # your email address
SMTP_PASS = ""          # app password (not your regular password)
FROM_NAME = ""          # your display name
FROM_EMAIL = ""         # your email address

ARCHIVE_URL = "[ARCHIVE URL — replace after uploading to archive.org]"
YOUR_NAME = "[YOUR NAME]"
SEND_DATE = datetime.now().strftime("%d %B %Y")

PDF_PATH = r"C:\Users\Tia_r\Downloads\10_PEOPLE_BEFORE_NUREMBERG_1_PERSON_AFTER.pdf"

CONTACTS_DIR = r"C:\Users\Tia_r\campaign_contacts"
LOG_FILE = r"C:\Users\Tia_r\campaign_contacts\send_log.csv"
TRACKING_FILE = r"C:\Users\Tia_r\campaign_contacts\campaign_tracking.csv"

# Rate limit: seconds between emails
RATE_LIMIT = 5

# Federal CC list (on every formal notice email)
FEDERAL_CC = [
    "complaints@humanrights.gov.au",
    "info@ombudsman.gov.au",
    "alrc@alrc.gov.au",
    "infocentre@accc.gov.au",
]

# ---------------------------------------------------------------------------
# Email Templates
# ---------------------------------------------------------------------------

TEMPLATES = {
    # Formal notice for oversight bodies - Version A (no links, no attachments)
    "oversight_A": {
        "subject": "Formal Notice of Evidence — Systemic Misconduct — Criminal Justice Methodology",
        "body": """To {recipient_name},

I write to provide formal notice of evidence bearing directly on your jurisdiction.

The evidence I am submitting establishes the following as documented fact:

Human deception detection — the credibility assessment framework used in every interrogation, every courtroom, every parole assessment in this jurisdiction — operates at 54.1% accuracy. Chance is 50%. For lie detection specifically the rate is 47% — below chance. This was established by Bond and DePaulo (2006) across 206 studies and 24,483 judges and has not been meaningfully contradicted since.

91.3% of the behavioural cues used by investigators to assess credibility are either empirically unrelated to deception or directionally inverted. Binomial test result: p < 0.0001.

Pre-interrogation detention conditions produce a compound elevation in suggestibility of 80 to 120% above baseline before the first question is asked.

Between 12% and 30% of persons exonerated by DNA evidence had confessed to crimes they did not commit.

These findings establish that every officer who has conducted a credibility assessment, obtained a confession under custody conditions, or participated in the process of detention and prosecution after this evidence existed has done so in the context of a methodology documented to be structurally unreliable.

I am providing this notice formally and in writing so that the record reflects the date on which this evidence was received. What is done with it from this point is now a documented choice.

I am available to provide the full evidentiary documentation on request.

Yours faithfully,
{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Formal notice - Version B (with archive link)
    "oversight_B": {
        "subject": "Formal Notice of Evidence — Systemic Misconduct — Criminal Justice Methodology",
        "body": """To {recipient_name},

I write to provide formal notice of evidence bearing directly on your jurisdiction.

The full evidentiary record, including original statistical analyses, meta-analytic synthesis, and a complete statement of findings, has been permanently archived at:

{archive_url}

The document is titled: 10 People Before Nuremberg. 1 Person After.

In summary, the evidence establishes that the credibility assessment framework used in every interrogation and every courtroom operates at chance level, that 91.3% of the cues used to assess guilt point in the wrong direction, that pre-interrogation custody conditions compromise the voluntariness of confessions before questioning begins, and that between 12% and 30% of DNA exonerations involve false confessions.

This notice is formal and written. The record reflects the date it was received. What is done with it from this point is a documented choice.

Yours faithfully,
{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Formal notice - Version C (with PDF attached)
    "oversight_C": {
        "subject": "Formal Notice of Evidence — Systemic Misconduct — Criminal Justice Methodology [Document Attached]",
        "body": """To {recipient_name},

I write to provide formal notice of evidence bearing directly on your jurisdiction.

The full evidentiary record has been permanently archived at:

{archive_url}

The document is titled: 10 People Before Nuremberg. 1 Person After.

The complete document is attached to this email as a PDF. It contains the full statistical analysis, original research findings, and the complete series of papers constituting the evidentiary record.

In summary: the credibility assessment framework used across the Australian justice system operates at chance level (54.1%), 91.3% of behavioural cues used to assess guilt are empirically inverted, pre-interrogation conditions compromise voluntariness, and 12-30% of DNA exonerees confessed falsely.

This notice is formal and written. The record reflects the date it was received.

Yours faithfully,
{your_name}
{date}""",
        "attach_pdf": True,
    },

    # Advocate recruitment (different tone)
    "advocate": {
        "subject": "Evidence-based justice reform — looking for the right path forward",
        "body": """Hi,

I'm writing because someone I care about went through the criminal justice system in Western Australia and what happened to her in custody was documented — stripping, isolation, denial of basic hygiene, a clinical psychologist using her Functional Neurological Disorder symptoms as evidence she was faking.

She wrote it down. Not as a victim statement. As an evidentiary argument.

The document is called 10 People Before Nuremberg. 1 Person After. It compiles the peer-reviewed research on credibility assessment (Bond & DePaulo, 2006 — 54.1% accuracy, chance is 50%), false confessions (12-30% of DNA exonerees confessed), and the 91.3% inversion rate of behavioural cues used to assess guilt.

The document has been permanently archived at: {archive_url}

I've also compiled a contact database of 524 people across the Australian justice system — judges, court registries, oversight bodies, DPPs, ombudsmen, anti-corruption commissions, law societies, and academics.

I want to know what actually works. That's why I'm writing to you first.

1. Is there a strategic litigation path here?
2. Is there an existing inquiry or reform process this evidence should go to?
3. Would your organisation be willing to look at the document and tell me honestly whether it has legs?

This isn't a complaint. It's a person with evidence, a distribution list, and a willingness to do the work — looking for someone who knows which door to knock on.

Thank you for your time.

{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Media pitch
    "media": {
        "subject": "Investigation pitch: The science says the justice system's core tool doesn't work",
        "body": """Hi,

A 28-page document called "10 People Before Nuremberg. 1 Person After" has been formally submitted to every oversight body in every Australian jurisdiction.

It compiles fifty years of peer-reviewed research establishing that the credibility assessment framework used in every Australian courtroom and interrogation room operates at chance level — 54.1% accuracy against 50% chance. It documents that 91.3% of the behavioural cues used to assess guilt are empirically inverted. It connects this to a specific person's experience in Western Australian custody: a woman with Functional Neurological Disorder whose symptoms were used by a psychologist as evidence of fabrication.

The document includes a cost-benefit analysis: Australia spends $32 billion annually on a justice system with 40-50% recidivism. Nordic models achieve 20-25% for less.

The document has been permanently archived at: {archive_url}

The person who wrote it is willing to speak on the record.

I'm happy to provide the full document, the research citations, and the contact database of 524 justice system personnel it has been or will be sent to.

{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Academic submission
    "academic": {
        "subject": "Submission of evidence — credibility assessment methodology and wrongful conviction",
        "body": """Dear {recipient_name},

I write to draw your attention to a document that may be relevant to your research.

"10 People Before Nuremberg. 1 Person After" is a 28-page evidentiary argument establishing that the credibility assessment methodology used across the Australian criminal justice system is structurally unreliable, drawing on Bond & DePaulo (2006), the Global Deception Research Team (2006), DePaulo et al. (2003), Gudjonsson & Clark (1986), and the National Registry of Exonerations.

The document includes an original cross-referencing analysis (Belief-Reality Inversion Matrix) finding that 91.3% of commonly believed deception cues are empirically unrelated to or inversely correlated with actual deception (binomial test p < 0.0001).

It also documents a specific case in Western Australia involving a person with Functional Neurological Disorder whose condition-consistent presentation was used as clinical evidence of fabrication.

The document has been permanently archived at: {archive_url}

If this intersects with your research interests, I would welcome any assessment of the evidentiary argument's validity.

Yours sincerely,
{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Law reform commission submission
    "law_reform": {
        "subject": "Formal Submission — Evidence-Based Reform — Criminal Justice Credibility Assessment",
        "body": """To {recipient_name},

I write to make formal submission of evidence requiring urgent law reform across Australian criminal justice jurisdictions.

The submission establishes, through peer-reviewed meta-analytic evidence and original statistical analysis, that the foundational methodology of criminal justice — credibility assessment — operates at chance level and is systematically inverted relative to the empirical evidence on deception.

The specific reforms required by this evidence are:

1. The prohibition of credibility assessment as determinative evidence in criminal proceedings.
2. The mandatory disclosure to juries of the empirical limitations of credibility assessment.
3. The exclusion of confessions obtained under pre-interrogation custody conditions documented to compromise voluntariness.
4. The recognition of autism spectrum disorder and Functional Neurological Disorder as protected characteristics requiring specific procedural accommodation.
5. A formal review of all convictions obtained primarily on confession evidence obtained under Reid Technique conditions.

The full evidentiary basis has been permanently archived at: {archive_url}

This submission is provided formally and in writing.

Yours faithfully,
{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Courts/judges — informational
    "courts": {
        "subject": "Formal Notice — Peer-Reviewed Evidence on Credibility Assessment Methodology",
        "body": """To {recipient_name},

I write to provide formal notice of peer-reviewed evidence bearing on the credibility assessment methodology used in proceedings before this court.

Bond and DePaulo (2006) established across 206 studies and 24,483 judges that human deception detection operates at 54.1% accuracy against a 50% chance baseline. For lie detection specifically: 47% — below chance.

Cross-referencing the Global Deception Research Team (2006) belief data against DePaulo et al. (2003) effect-size literature across 23 matched cues establishes that 91.3% of behavioural cues used to assess credibility are either empirically unrelated to deception or directionally inverted (binomial test p < 0.0001).

The full evidentiary record has been permanently archived at: {archive_url}

This notice is provided formally and in writing.

Yours faithfully,
{your_name}
{date}""",
        "attach_pdf": False,
    },

    # Generic/other
    "generic": {
        "subject": "Formal Notice of Evidence — Criminal Justice System Methodology",
        "body": """To {recipient_name},

I write to provide formal notice of peer-reviewed evidence establishing that the credibility assessment methodology used across the Australian criminal justice system operates at chance level.

The full evidentiary record has been permanently archived at: {archive_url}

This notice is provided formally and in writing.

Yours faithfully,
{your_name}
{date}""",
        "attach_pdf": False,
    },
}

# Map categories to templates
CATEGORY_TEMPLATE_MAP = {
    "1_advocates": "advocate",
    "2_media": "media",
    "3_academics": "academic",
    "4_oversight": "oversight_A",  # default to version A
    "5_government": "oversight_A",
    "6_legal_profession": "generic",
    "7_courts_judges": "courts",
    "8_tribunals": "courts",
    "9_gov_council": "generic",
    "10_gov_purchasing": "generic",
    "11_other": "generic",
}


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def load_contacts(category):
    """Load contacts from a category CSV."""
    filepath = os.path.join(CONTACTS_DIR, f"{category}.csv")
    if not os.path.exists(filepath):
        print(f"ERROR: {filepath} not found")
        sys.exit(1)
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fill_template(template, contact):
    """Fill template placeholders with contact data."""
    name = contact.get("name", "")
    court = contact.get("court", "")
    recipient = name if name else court if court else "whom it may concern"

    body = template["body"].format(
        recipient_name=recipient,
        archive_url=ARCHIVE_URL,
        your_name=YOUR_NAME,
        date=SEND_DATE,
    )
    subject = template["subject"]
    return subject, body


def build_email(to_addr, subject, body, cc_list=None, attach_pdf=False):
    """Build MIME email message."""
    msg = MIMEMultipart()
    msg["From"] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg["To"] = to_addr
    msg["Subject"] = subject
    if cc_list:
        msg["Cc"] = ", ".join(cc_list)

    msg.attach(MIMEText(body, "plain", "utf-8"))

    if attach_pdf and os.path.exists(PDF_PATH):
        with open(PDF_PATH, "rb") as f:
            pdf = MIMEApplication(f.read(), _subtype="pdf")
            pdf.add_header("Content-Disposition", "attachment",
                           filename="10_People_Before_Nuremberg_1_Person_After.pdf")
            msg.attach(pdf)

    return msg


def log_send(contact, category, template_name, version, status, error=None):
    """Log send attempt to CSV."""
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "email", "name", "court", "jurisdiction",
                            "category", "template", "version", "status", "error"])
        writer.writerow([
            datetime.now().isoformat(),
            contact.get("email", ""),
            contact.get("name", ""),
            contact.get("court", ""),
            contact.get("jurisdiction", ""),
            category,
            template_name,
            version,
            status,
            error or "",
        ])


def send_email(msg, to_addr):
    """Send email via SMTP."""
    if not SMTP_HOST or not SMTP_USER or not SMTP_PASS:
        print("ERROR: SMTP settings not configured. Edit the script first.")
        sys.exit(1)

    recipients = [to_addr]
    if msg["Cc"]:
        recipients += [addr.strip() for addr in msg["Cc"].split(",")]

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(FROM_EMAIL, recipients, msg.as_string())


def list_categories():
    """List available contact categories."""
    print("\nAvailable categories:\n")
    for fname in sorted(os.listdir(CONTACTS_DIR)):
        if fname.endswith(".csv") and not fname.startswith("send_log") and not fname.startswith("campaign_tracking"):
            cat = fname.replace(".csv", "")
            contacts = load_contacts(cat)
            template = CATEGORY_TEMPLATE_MAP.get(cat, "generic")
            print(f"  {cat:<25} {len(contacts):>4} contacts  (template: {template})")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Campaign mail-merge sender")
    parser.add_argument("--category", help="Contact category to send to (e.g. 1_advocates)")
    parser.add_argument("--version", choices=["A", "B", "C"], default="A",
                       help="Template version for oversight emails (A=no links, B=with link, C=with PDF)")
    parser.add_argument("--template", help="Override template name (e.g. advocate, media, academic)")
    parser.add_argument("--dry-run", action="store_true", help="Preview emails without sending")
    parser.add_argument("--preview", action="store_true", help="Preview single email")
    parser.add_argument("--to", help="Preview email for specific address")
    parser.add_argument("--list", action="store_true", help="List available categories")
    parser.add_argument("--no-cc", action="store_true", help="Skip federal CC list")
    parser.add_argument("--limit", type=int, help="Max emails to send")

    args = parser.parse_args()

    if args.list:
        list_categories()
        return

    if not args.category and not args.preview:
        parser.print_help()
        return

    # Determine template
    if args.template:
        template_name = args.template
    elif args.category:
        template_name = CATEGORY_TEMPLATE_MAP.get(args.category, "generic")
        # Handle oversight versions
        if template_name.startswith("oversight") and args.version:
            template_name = f"oversight_{args.version}"
    else:
        template_name = "generic"

    if template_name not in TEMPLATES:
        print(f"ERROR: Unknown template '{template_name}'")
        print(f"Available: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    template = TEMPLATES[template_name]

    # Load contacts
    if args.preview and args.to:
        contacts = [{"name": "Preview Recipient", "email": args.to, "court": "", "jurisdiction": ""}]
    elif args.category:
        contacts = load_contacts(args.category)
    else:
        parser.print_help()
        return

    if args.limit:
        contacts = contacts[:args.limit]

    # CC list
    cc_list = [] if args.no_cc else FEDERAL_CC
    # Don't CC federal bodies on advocate/media emails
    if template_name in ("advocate", "media"):
        cc_list = []

    print(f"\n{'DRY RUN — ' if args.dry_run else ''}Campaign Send")
    print(f"Category: {args.category or 'preview'}")
    print(f"Template: {template_name}")
    print(f"Contacts: {len(contacts)}")
    print(f"CC list:  {', '.join(cc_list) if cc_list else 'none'}")
    print(f"PDF:      {'attached' if template.get('attach_pdf') else 'no'}")
    print("-" * 60)

    sent = 0
    failed = 0

    for i, contact in enumerate(contacts):
        email = contact.get("email", "").strip()
        if not email:
            continue

        subject, body = fill_template(template, contact)
        msg = build_email(email, subject, body, cc_list, template.get("attach_pdf", False))

        if args.dry_run or args.preview:
            print(f"\n{'='*60}")
            print(f"TO:      {email}")
            print(f"SUBJECT: {subject}")
            if cc_list:
                print(f"CC:      {', '.join(cc_list)}")
            print(f"PDF:     {'yes' if template.get('attach_pdf') else 'no'}")
            print(f"{'-'*60}")
            print(body[:500])
            if len(body) > 500:
                print(f"... [{len(body)} chars total]")
            print(f"{'='*60}")
            log_send(contact, args.category or "preview", template_name, args.version, "dry_run")
            sent += 1
        else:
            try:
                send_email(msg, email)
                log_send(contact, args.category, template_name, args.version, "sent")
                sent += 1
                print(f"  [{sent}/{len(contacts)}] SENT: {email}")
            except Exception as e:
                log_send(contact, args.category, template_name, args.version, "failed", str(e))
                failed += 1
                print(f"  [{sent+failed}/{len(contacts)}] FAILED: {email} — {e}")

        # Rate limit between sends
        if not args.dry_run and not args.preview and i < len(contacts) - 1:
            time.sleep(RATE_LIMIT)

    print(f"\nDone. Sent: {sent}, Failed: {failed}")
    if not args.dry_run and not args.preview:
        print(f"Log: {LOG_FILE}")


if __name__ == "__main__":
    main()
