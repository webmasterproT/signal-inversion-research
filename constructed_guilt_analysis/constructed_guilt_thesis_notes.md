# OMXUS Thesis Working Notes
## 20,000 Word Thesis: "Sanctuary Design — A Zoological Framework for Human Systems"

**Date:** 2026-03-01
**Status:** Research & Planning Phase

---

## I. CORE THESIS STATEMENT

**If humans were a newly discovered species arriving at a well-designed sanctuary, would we design their enclosure the way current civilization is structured?**

The answer is demonstrably no. Every component of current human systems — governance, justice, economics, safety, nutrition — violates basic principles any competent zookeeper would apply to any other species.

The OMXUS system proposes a redesign based on:
1. What the animal actually needs (the 8 life areas)
2. What scale the animal can operate at (Dunbar's 150)
3. What technology enables without requiring utopian human nature

---

## II. KEY EVIDENCE SOURCES

### A. Philosophy & Framework
- **MANIFESTO.md** — Core problem diagnosis: insulation from consequences
- **PRINCIPLES.md** — 6 non-negotiable constraints (individual freedom, non-maleficence, prevention-only justice, transparent accountability, telemetry for humans, zero friction)
- **zookeeper-structure.md** — The narrative frame (Applebee's Report, ~133,000 word book structure)

### B. The Token System (Chapter 17)
**Core insight:** Current identity systems depend on central authority (governments). 1 billion humans invisible because state hasn't documented them.

**Web of Trust model:**
- 3 existing verified humans vouch for you
- Physical proximity verified via NFC/mesh
- Social cost to fraud (reputation at stake in community of 150)
- Sybil-resistant without central authority

**Distribution principle:**
```
Resources available ÷ Number of verified humans = Share per human
```
Not proportional to "contribution" — existence alone qualifies.

**Cryptographic anchoring:**
- State committed to Bitcoin blockchain (immutable)
- OP_RETURN: TAG(4) + EPOCH(4) + ROOT(32) = 40 bytes per anchor
- No government can erase an identity

**LIVE CONTRACTS (already built):**

`OMXUSHER.sol` — Human Existence Record (Soulbound NFT):
```solidity
// Key features:
- error Soulbound();                    // Cannot transfer
- error AlreadyVerified(address human); // One per human
- 3 vouches = automatic verification
- Trust score with ripple responsibility (1/3 propagates to vouchers)
- bootstrapVerify() for genesis humans
```

`OMXUSVoteAnchor.sol` — Vote Merkle Root Anchoring:
```solidity
// Votes cast off-chain via mesh, signed with HER Ed25519 keys
// On close: all votes hashed into MMR, root committed on-chain
// Any voter can prove inclusion via verifyVoteInclusion()
// Cost: ~$0.22 L1, ~$0.005 Base L2
```

This isn't theory. The code exists.

### C. The Ring & Emergency Response (Chapter 16)
**The problem quantified:**
- Cardiac arrest: 4-minute survival window
- Ambulance arrival: 7-14 minutes (best case, urban)
- Gap: 10 minutes of dying

**Existing proof-of-concept:**
- Hatzalah (Jewish volunteer network): < 3 minutes response
- GoodSAM (UK/Australia): ~ 6 minutes median
- PulsePoint (USA): 4,500+ communities

**Ring design:**
- $9 NFC smart ring (no battery, waterproof)
- Gross motor activation (tap pattern works under stress)
- Silent for DV scenarios
- Alert goes to ALL token holders within 1km
- Estimated response: 15-25 seconds (20% urban adoption)

**Structural DV elimination:**
Current system enables DV through: isolation, secrecy, slow response, victim not believed.
Community of 150 eliminates: isolation impossible, patterns visible, 60-second response, witnesses arrive.

### D. Diet Research — Environmental Determinism of Health

**KITAVA ISLANDERS (Papua New Guinea)**
- Source: Lindeberg et al., 1,200 subjects
- Diet: 69% carbs (tubers), 21% fat (coconut), 10% protein
- **ACNE: 0% of 300 adolescents** (vs 79-95% Western)
- CVD: Zero despite 76-80% smoking
- Diabetes: Zero
- BMI: ~19 despite food abundance
- Fasting insulin: 50% of Swedish levels

**Mechanism:** Not low-carb. High-carb but LOW glycemic load (unprocessed tubers).
Hyperinsulinemia cascade: high GI → chronic high insulin → IGF-1 → androgen → sebum → acne

**INUIT (Pre-contact)**
- Diet: ~90% fat/protein (marine mammals, fish, organs)
- Polar opposite of Kitava
- Same outcome: Zero acne, zero CVD, zero diabetes
- Then: flour, sugar, canned goods arrived → every disease within ONE generation

**OKINAWA**
- Diet: 90% whole plant foods, 60% calories from sweet potato
- Hara hachi bu (eat 80% full)
- Results: Lowest heart disease, cancer, dementia in industrialized world
- Most centenarians per capita globally
- Real-time experiment: Elders (traditional diet) living to 105+, their children (American diet) now highest obesity in Japan

**THE PATTERN:**
Food matching organism's biology = disease disappears.
Supply chain replacing browse = every disease appears.

**Zoological frame:** Sydney Zoo tests 49 compounds in eucalyptus for koalas. Kitavans don't need testing because nobody replaced their browse. Humans accepted being fed food optimized for profit, not health.

### E. Mesh Network — Infrastructure Sovereignty

**VexConnect Protocol:**
```
Phone A ──BLE──▶ Phone B ──BLE──▶ Phone C ──WiFi──▶ Internet
```

- Every phone is both peripheral (advertiser) and central (scanner)
- Packets: Version(1) + PacketID(8) + TTL(1) + Flags(1) + Payload(501) = max 512 bytes
- TTL starts at 7, decrements each hop
- Deduplication via 60-second cache (prevents loops)
- NaCl encryption (X25519 + XSalsa20 + Poly1305)

**Why it matters:**
- Works offline (no ISP required)
- No central server to shut down
- No company to sue
- Every phone extends network for neighbors
- At 1% adoption: neighborhood-level connectivity
- At 10% adoption: city-level mesh possible

**3-Layer Architecture:**
```
Layer 1: Bitcoin (immutable anchor)
Layer 2: HER/IPFS (distributed identity)
Layer 3: Mesh Network (communication)
Physical: NFC Ring (interface)
```

---

## III. THE CORE ARGUMENTS

### Argument 1: Insulation From Consequences
**Current:** Decision-makers don't experience outcomes.
- Politicians vote on laws for communities they've never visited
- Judges sentence people to conditions they've never experienced
- Police "protect" people they don't know and aren't accountable to

**Result:** Systems optimize for the decision-maker's convenience, not the affected party's welfare.

**Solution:** Proximity-weighted voting + empathy invitations (swap lives for 7 days when you can't agree).

### Argument 2: Scale Problem (Dunbar's Number)
**Constraint:** Human brain can maintain ~150 meaningful relationships (hard biological limit).
- Village of 150 → trust works naturally
- City of 1 million → trust breaks → substitutes needed (contracts, lawyers, police)
- Substitutes don't satisfy the animal → dysfunction

**Solution:** Small overlapping trust clusters (150 or fewer), networked. "The parish council without the passive aggression."

### Argument 3: Prevention vs Punishment
**Current:** Justice = harm happens → punish (45% recidivism)
**Proposed:** Justice = prevention only (structural impossibility of harm)

**Prevention mechanisms:**
1. Universal witness (never isolated in community of 150)
2. Instant response (60 seconds vs 20 minutes)
3. Cryptographic accountability (actions signed, attribution certain)
4. Proximity responsibility (nearby people MUST help)
5. Economic alternative (everyone earns legitimately)

### Argument 4: Environmental Determinism
**Evidence:** Language acquisition proves environment determines outcomes (Cohen's h = 0.93, 1.8B sample).
**Implication:** If environment determines language, it determines behavior. Current systems create violence through environmental design, not human nature.

---

## IV. PROPOSED THESIS STRUCTURE (20,000 words)

### Part I: The Problem (5,000 words)

**Chapter 1: You Are A Zookeeper (1,500 words)**
- The conceit: if assigned the human enclosure, what would you observe?
- Current systems viewed through zoo ethics
- The question: "Would you design it this way?"

**Chapter 2: What The Animal Needs (1,500 words)**
- The 8 life areas framework
- Vehicle (body), Cub (play), Herd Member (connection), God (creation), Slave (service), Master (mastery), Monk (meaning), Zookeeper (habitat)
- Independence test: can flourish in 7, suffer in 8th
- Dunbar's number as hard constraint

**Chapter 3: What They Actually Built (2,000 words)**
- Token system (money from nothing, 8 humans > 4 billion)
- Justice system (revenge with a wig)
- Education (13 years sitting still)
- Governance (lawyers deciding engineering)
- Scale problem: every system worked at 150, broke at civilization

### Part II: The Evidence (5,000 words)

**Chapter 4: Environmental Determinism — Diet as Proof (2,500 words)**
- Kitava: 69% carbs, zero acne, zero CVD, zero diabetes
- Inuit: 90% fat, same outcomes, until flour arrived
- Okinawa: sweet potato majority, most centenarians
- Nauru: traditional → processed food → 40% diabetes in one generation
- Mechanism: not carbs vs fat, but processed vs whole
- Zoological frame: koalas get 49-compound testing, humans get supply chain

**Chapter 5: The Trust Deficit — Current Systems (2,500 words)**
- Bradley Edwards case: system had him, released him, three women dead
- Emergency response: 4-minute window, 14-minute arrival
- DV dynamics: isolation, secrecy, slow response, victim not believed
- Bystander effect research: diffusion of responsibility, pluralistic ignorance, evaluation apprehension
- Why existing systems can't solve this (architecture, not funding)

### Part III: The Solution (6,000 words)

**Chapter 6: The Token (2,000 words)**
- Web of trust: 3 vouchers, physical proximity, social cost to fraud
- No government required (1 billion currently invisible to state systems)
- Equal distribution: existence qualifies, not contribution
- Bitcoin anchoring: can't be erased
- Objections answered: freeloading (Ostrom's commons research), scarcity (distribution not production)

**Chapter 7: The Ring & Safety Network (2,000 words)**
- $9 NFC ring, gross motor activation
- 15-25 second response (vs 7-14 minutes)
- Existing evidence: Hatzalah (3 min), GoodSAM (6 min), PulsePoint (4,500 communities)
- DV structural elimination: isolation impossible, patterns visible, witnesses arrive
- Trust signal: the knowledge changes the experience

**Chapter 8: The Infrastructure (2,000 words)**
- 3-layer architecture: Bitcoin anchor, HER/IPFS identity, Mesh network
- VexConnect protocol: BLE mesh, every phone a router
- Why unkillable: no central server, no company, distributed data
- 1% adoption threshold for ISP-independence
- Governance: proximity-weighted voting, empathy invitations, rotating service

### Part IV: Implications (4,000 words)

**Chapter 9: Why It Works Together (1,500 words)**
- Each component addresses same root causes
- Token enables counting → enables distribution → enables emergency network
- Ring requires identity → requires community → requires trust
- Mesh requires participation → incentivized by value received
- Feedback loops: more members → more safety → more trust → more members

**Chapter 10: The Viability Question (1,500 words)**
- Every component exists (Bitcoin 15 years, NFC everywhere, mesh decades old)
- Not utopian (doesn't require better humans, just different conditions)
- Buildable with current technology
- Replicability: 52-item scaffold for rapid deployment
- What makes it different: integrated system vs piecemeal reform

**Chapter 11: If Humans Were New (1,000 words)**
- The thought experiment: newly discovered species
- Would any zookeeper design current systems?
- The answer informs what we should build
- Conclusion: systems engineering, not idealism

---

## V. KEY CITATIONS TO INCLUDE

**Dunbar's Number:**
- Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. *Journal of Human Evolution*, 22(6), 469-493.

**Bystander Effect:**
- Latané, B., & Darley, J. M. (1968). Group inhibition of bystander intervention in emergencies. *Journal of Personality and Social Psychology*, 10(3), 215-221.

**Collective Efficacy:**
- Sampson, R. J., Raudenbush, S. W., & Earls, F. (1997). Neighborhoods and violent crime: A multilevel study of collective efficacy. *Science*, 277(5328), 918-924.

**Kitava/Diet:**
- Lindeberg, S. (2010). *Food and Western Disease*. Wiley-Blackwell.
- Cordain, L., Lindeberg, S., et al. (2002). Acne Vulgaris: A Disease of Western Civilization. *Arch Dermatol*, 138(12), 1584-1590.

**Tsimane:**
- Kaplan, H., et al. (2017). Coronary atherosclerosis in indigenous South American Tsimane. *The Lancet*, 389(10080), 1730-1739.

**Commons Management:**
- Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.

**Bullshit Jobs:**
- Graeber, D. (2018). *Bullshit Jobs: A Theory*. Simon & Schuster.

**Emergency Response:**
- Hatzalah response time data
- GoodSAM deployment research
- PulsePoint community data

---

## VI. OPEN QUESTIONS FOR THESIS

1. **Bootstrapping:** ~~How do first 3 token holders get verified? Genesis event vulnerability.~~

   **RESOLVED:** Video the genesis event. Document the first token holders publicly. After that, cryptographic linking to vouchees creates permanent accountability chain. If your vouchee causes harm, responsibility propagates to you — this is the enforcement mechanism.

   **Key evidence:** Australia has registered voters WITHOUT ID since 1924. Australians vote WITHOUT ID. The "but how do you verify?" objection assumes government ID is necessary — it demonstrably isn't. Social verification (someone in your community knows you) has worked for a century in a modern democracy.

2. **Empathy failure modes:** ~~What if living someone's life increases contempt?~~

   **RESOLVED:** If people are calling 150-person meetings, swapping lives via ViewSwap, and STILL can't work it out — why? What's actually going on there? The mechanism is **boredom as enforcement**. Endless meetings until compromise is found. People will eventually find something they can live with because the alternative is more meetings.

   This is aikido: use the thing people hate (meetings) to create the thing people want (resolution).

3. **Emergency decisions:** ~~Some things need NOW decisions. Delegate systems with pre-authorized authority?~~

   **RESOLVED:** Yes — similar to volunteer firefighters.

   Key insight: **Young men especially WANT to serve.** Look at:
   - Volunteer firefighters (massive participation)
   - Call of Duty (interesting title — the desire for meaningful duty is so strong they simulate it)
   - Basic solidarity examples everywhere

   French concept: **emergency obligation** — civic duty to respond.

   OMXUS version: **Every token holder is pre-authorized.** The web of trust IS the authorization. You don't need a separate delegate system — the community IS the emergency response system.

4. **Adoption curve:** ~~What's the minimum viable community size?~~

   **RESOLVED:** Does it matter?
   - How many of us vote on Meta every week? (Billions. Secure online voting exists.)
   - How many of us have 3 friends? (Almost everyone.)
   - How many would volunteer 1x per year if 1 in 10 needed to participate?

   **The real comparison:** Current system costs $32 billion and achieves 45% recidivism. The bar for "viable alternative" is extraordinarily low.

5. **Interface with existing systems:** Building now.
   - iOS apps in development (anchor-ios, vexconnect-ios)
   - Web app: https://webapp-omxus.tiation.workers.dev/dashboard
   - Contracts: omxus-main/contracts

6. **Enforcement without punishment:** If prevention fails, what then? Contained community with dignity, but how enforced?

---

## VII. KEY RHETORICAL POINTS FOR THESIS

**"The bar is extraordinarily low"**
Current system: $32 billion/year → 45% recidivism, dead women.
Proposed system: Almost nothing → might actually work.
The comparison isn't "perfect alternative" vs "imperfect status quo." It's "attempt at improvement" vs "known failure."

**"Boredom as enforcement"**
When empathy invitations fail, endless meetings until compromise. Aikido: use what people hate (meetings) to create what they want (resolution).

**"Call of Duty" observation**
The desire for meaningful service is so strong they SIMULATE it in video games. Young men want duty. Volunteer firefighters prove this. The system just needs to channel it.

**"100 years without ID"**
Australia has registered voters and run elections without ID since 1924. The "but how do you verify identity?" objection is empirically refuted by a century of functioning democracy.

**"Everyone is pre-authorized"**
French emergency obligation concept. Web of trust IS authorization. No separate delegate system needed — community IS the emergency response.

**"How many of us have 3 friends?"**
Almost everyone. The system's minimum viable requirement is laughably achievable.

---

## VIII. DESIGN METHODOLOGY: "HOW WILL THEY FEEL IT?"

### The Sales Insight Academia Forgot

People don't buy arguments. They buy felt difference.

| Approach | Result |
|----------|--------|
| "Here's why you should want this" | Resistance |
| "Here's what happens when you use it" | Adoption |

The thesis doesn't need to convince everyone the system is good. It needs to describe a system that provides immediate value.

### Efficiency in the TRUE Sense

| False Efficiency | True Efficiency |
|------------------|-----------------|
| Extract maximum from each interaction | Achieve goal with minimum friction |
| Optimize for the metric | Optimize for the outcome |
| Convince everyone first | Provide value, argument follows |
| 38+ hours for some, 0 for others | <28 hours for everyone who's able |
| $32B and 45% recidivism | $0, 60-second response, men have purpose and meaning, we stop hurting each other, we connect |

Current systems are efficient at extraction. Not efficient at the stated goal.

### The Universal Appeal

The capuchin doesn't have a theory about fairness. It throws the cucumber.

- 35 million years before religion
- Before economics
- Before race as a concept
- Before ideology

**The flatearther and the physicist both speak English.** They disagree about the earth's shape. They don't disagree about having learned language from their environment.

Mirror neurons don't check your ideology. Stalin believed in communism. He ended up unable to trust his daughter.

### The Felt Experience of Each Component

| Component | What they feel |
|-----------|----------------|
| Token | "I exist and that's enough" |
| Ring | "Someone came in 60 seconds" |
| Community | "These 150 people actually know me" |
| Income | "I didn't grovel for it" |

Not: "Here's the cryptographic proof."
But: "Someone came."

### Why This Works Across All Groups

The thesis doesn't say "here's why your group should care."

It says: "This is how animals work. You're an animal. Here's what happens when you build for the animal."

The flatearther will take the money. The billionaire will take the safety. The argument happens *after* the value arrives.

---

## IX. WRITING APPROACH

**Voice:** Academic but accessible (not jargon-heavy)
**Frame:** Systems engineering, not ideology
**Method:**
- Present evidence first
- Show what exists already (Hatzalah, Kitava, etc.)
- Demonstrate integration
- Address objections inline

**Avoid:**
- Utopianism accusations (emphasize existing technology)
- Human nature debates (emphasize environmental determinism evidence)
- Political alignment (this isn't left/right, it's systems design)

---

## IX. NEXT STEPS

1. [ ] Finalize chapter word allocations
2. [ ] Gather additional academic citations
3. [ ] Draft Introduction (establish the zookeeper frame)
4. [ ] Write Part I (The Problem)
5. [ ] Write Part II (The Evidence)
6. [ ] Write Part III (The Solution)
7. [ ] Write Part IV (Implications)
8. [ ] Review for internal consistency
9. [ ] Final edit pass

---

## X. THESIS WORD COUNT ALLOCATION

| Section | Words | % |
|---------|-------|---|
| Part I: The Problem | 5,000 | 25% |
| Part II: The Evidence | 5,000 | 25% |
| Part III: The Solution | 6,000 | 30% |
| Part IV: Implications | 4,000 | 20% |
| **Total** | **20,000** | **100%** |

---

---

## XI. ADDITIONAL EVIDENCE FOR THESIS (New Material)

### A. The Language Proof (Original Research)
**File:** `omxus-main/research/is_our_language_determined_by_our_birth_country/Cross_National_Language_Acquisition_Study.md`

**Sample:** 1.8 billion individuals across 9 countries
**Effect size:** Cohen's h = 0.93 (mean) — exceeds "large" threshold of 0.80
**Finding:** Geographic residence predicts language with 72-97% accuracy

**The punchline (academic deadpan):**
> "The finding that 'people speak the language where they live' may seem trivially obvious, but the magnitude of the effect—and its potential implications for understanding human behavioural acquisition more broadly—may be less obvious than the finding itself."

**Implication:** If environment determines the most complex cognitive behavior (language), what does this suggest about simpler behaviors (aggression, emotional responses)?

### B. Two Washing Machine Theory (False Scarcity)
**File:** `wiki.omxus.com/content/concepts/Two_Washing_Machine_Theory.wiki`

**The problem:** Competition mandates waste.
- Company A makes a machine lasting 20 years → sells 1
- Company B makes a machine lasting 3 years → sells 6
- Company A goes bankrupt despite superior product

**The numbers:**
- 30 pounds of steel per washing machine
- 800 kWh to produce (enough to power a home for a year)
- Thrown away 2-3 years after purchase

**Broader applications:** Smartphones, printers, clothing, automobiles, light bulbs (Phoebus Cartel mandated 1,000-hour lifespan when 2,500+ was achievable).

### C. Two Monkey Theory (Capuchin Cucumber Experiment)
**File:** `wiki.omxus.com/content/philosophy/Two_Monkey_Theory.wiki`

**de Waal & Brosnan (2003):** Two capuchins, adjacent enclosures, same task. One gets cucumber, one gets grape.
- Equal pay: 95% acceptance
- Unequal pay: 40% acceptance (some threw cucumber at researcher)

**Cross-species replication:** Chimpanzees, bonobos, dogs, corvids. Fairness instinct is 35+ million years old.

**The paradox:** If fairness is innate and the many outnumber the few, why do unequal arrangements persist?

**Answer:** Coordination problems, information asymmetry, psychological mechanisms (system justification, learned helplessness, preference falsification).

**OMXUS cucumber test:** Would a capuchin accept these terms? If equivalent contribution yields wildly different rewards, the system will face rejection.

### D. Crime Prevention Evidence
**File:** `wiki.omxus.com/content/research/Crime_Prevention_Research.wiki`

**Current system:**
- $400/day per prisoner
- 45% recidivism rate
- $32B/year on justice system
- 20+ minute average police response

**Portugal decriminalization (2001-2020):**
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Problematic drug users | 100,000 | 33,000 | -67% |
| Drug-induced deaths | 80/million | 4/million | -95% |
| HIV among PWID | 1,016 cases | 18 cases | -98% |
| Drug incarceration | 44% of prisoners | 15% | -66% |

**Switzerland heroin-assisted treatment:**
- 82% reduction in illicit heroin use
- 55% decrease in property crime
- Zero overdose deaths in supervised settings
- Each franc invested saved 2.16 francs

### E. Evidence Still Needed

**1. UK Gas Oven Suicides (Kreitman, 1976)** — ✓ RESOLVED (see Section XV)

**2. Eyes on Honesty Box (Bateson et al., 2006)** — ✓ RESOLVED (see Section XV)

**3. 50% BS Work / COVID Essential Workers** — ✓ RESOLVED (see Section XII)

**4. Mirror Neurons + Cost to Wealthy (Stalin)**
- Mirror neurons: we automatically feel what we do to others
- Stalin: didn't trust his own daughter by end, paranoid of everyone
- "If I hurt people, I know in the deepest part of my being that 'people hurt people' — my brain doesn't distinguish between 'people'"
- Rich suffer too in low-trust societies

### F. Key Rhetorical Additions

**"Eyes on the box"**
As simple as: picture of eyes stops candy theft. That's the entire crime prevention argument in one study.

**"Gas oven suicides"**
Crime doesn't necessarily remain when conditions change. Remove the method, remove the outcome.

**"Stalin's daughter"**
Even the most powerful person in the system cannot escape the cost of non-trust. The wealthy are not exempt.

**"19 hours"**
Not utopian — calculable. COVID proved it. The remaining 21+ hours are manufactured activity to justify the extraction mechanism.

---

## XII. THE 20-HOUR WEEK: AUSTRALIAN WORKFORCE ANALYSIS

### The Question
If we eliminated "bullshit jobs" (Graeber), how many hours per week would actually be needed to maintain civilization?

### Australian Workforce Composition (ABS 2020-2025)

**1. Survival Essentials (~4.3M workers, ≈33%)**

| Sector | Workers | Source |
|--------|---------|--------|
| Healthcare & social assistance | ~1.7M | ABS: 13% of workforce |
| Food supply chain | ~0.9M | Agriculture (~325k) + Food Retail (~600k) |
| Transport & logistics | ~0.7M | Transport, Postal, Warehousing |
| Energy, water, utilities | ~0.15M | Electricity, Gas, Water, Waste |
| Emergency services & defence | ~0.3M | ADF + Police + Fire/Emergency |
| Core government admin | ~0.5M | Public Admin (excluding defence/police) |

**2. Tourism & Hospitality (~1.5M workers, ≈12%)**

| Sector | Workers |
|--------|---------|
| Hospitality (cafés, pubs, restaurants, hotels) | ~0.9M |
| Airlines, travel agencies | ~0.1-0.15M |
| Arts, recreation, attractions | ~0.2M |
| Retail tied to tourism | ~0.3M |

**3. Economic-Viability Essentials (~2.2M workers, ≈15-20%)**

| Sector | Workers |
|--------|---------|
| Mining & resources | ~0.25M |
| Construction & infrastructure | ~1.0M |
| Finance, banking, insurance | ~0.7M |
| Export-critical manufacturing | ~0.3-0.5M |

**4. Hidden Essentials / Quiet Scaffolding (~1.2-2.5M)**

| Sector | Workers |
|--------|---------|
| Education | ~0.5-1.0M |
| Maintenance & infrastructure | ~0.3-0.7M |
| Governance & justice | ~0.2-0.4M |
| Research & innovation | ~0.15-0.25M |
| Non-tourist culture | ~0.05-0.15M |

### The Totals

| Category | Workers | % of Workforce |
|----------|---------|----------------|
| Survival essentials | ~4.3M | 33% |
| + Tourism bundle | ~1.5M | 12% |
| + Economic viability | ~2.2M | 15-20% |
| **Subtotal** | **~8.0M** | **~60%** |
| Hidden scaffolding | +1.2-2.5M | 10-20% |
| **Functional baseline** | **~9.0-10.5M** | **70-80%** |

**What's left: ~20-30% (~2.5-4.0M workers)** in roles Graeber tags as "bullshit" — corporate bureaucracy, duplication, inflated admin.

### Hours Required Per Week

| Bundle | Total Hours/Week | If Shared Across 13M |
|--------|------------------|---------------------|
| Survival only | ~160M | **12.3 h/wk** |
| Survival + tourism | ~217M | **16.7 h/wk** |
| + economic viability | ~304M | **23.4 h/wk** |
| + hidden essentials (Lean) | ~350M | **26.9 h/wk** |
| + hidden essentials (Balanced) | ~376M | **28.9 h/wk** |
| + hidden essentials (Generous) | ~399M | **30.7 h/wk** |

### Current Australian Labour Force (ABS July 2025)

| Metric | Number |
|--------|--------|
| Employed | 14,641,400 |
| Unemployed | 649,000 |
| Unemployment rate | 4.2% |
| Participation rate | 67.0% |
| Total labour force | ~15.3M |
| Adult population (18+) | ~20M |

### The Math: Where Does 20 Hours Come From?

Full bundle needs ~399M hours/week.

| Distribution | Hours/Week/Person |
|--------------|-------------------|
| Spread across employed (14.6M) | **27.3 h/wk** |
| Spread across labour force (15.3M) | **26.1 h/wk** |
| Spread across all adults (20M) | **20.0 h/wk** |

**The 20-hour week emerges when everyone participates.**

### The Implication

Current system: 38-hour weeks for some, 0 hours for others, significant portion doing work that produces nothing.

Alternative: 20-26 hours/week for everyone, no unemployment, no bullshit jobs.

**The question isn't "can we afford this?" — it's "why are we doing it the other way?"**

### References

- Australian Bureau of Statistics (ABS) Labour Force, Australia, Detailed, Quarterly (2020-2025)
- ABS, Australian Industry 2019-20
- ABS, Tourism Satellite Account 2019-20
- Bureau of Infrastructure and Transport Research Economics (BITRE), Aviation Statistics
- Graeber, D. (2018). *Bullshit Jobs: A Theory*
- ILO/OECD, COVID-19 and the world of work (2020-21)

---

## XIII. COST OF NON-TRUST (The Wealthy Suffer Too)

### The Washing Machine + Security Version

Same logic as Two Washing Machine Theory, but applied to security:

| Trust Level | Cost to Wealthy |
|-------------|-----------------|
| High trust | Walk freely, minimal security, relationships authentic |
| Low trust | Gated compounds, bodyguards, paranoid of own family |

### The Stalin Example

By the end, Stalin didn't trust his own daughter. The most powerful person in the system was a prisoner of the system.

**Mirror neuron logic:**
> "If I hurt people, I know in the deepest part of my being that 'people hurt people' — my brain doesn't distinguish between 'people'"

You cannot be unkind and not feel it. The wealthy are not exempt from the psychological cost of living in a low-trust society they helped create.

### The False Security Economy

Current system:
- Private security industry: $X billion
- Insurance industry: $X billion
- Locks, cameras, gates, walls
- Legal defense funds
- Tax avoidance infrastructure
- Reputation management

All of this is **protection against other humans** — a tax on non-trust.

In high-trust society: none of this is necessary.

### The Question for the Wealthy

Would you trade 30% of your wealth for:
- Walking anywhere safely
- Trusting everyone around you
- No need for security
- Authentic relationships (people don't want your money)
- Your children safe
- Sleep without paranoia

**Current system gives them wealth but denies them safety.**

OMXUS offers: slightly less wealth, dramatically more security.

---

## XV. ENVIRONMENTAL INTERVENTION EVIDENCE

### UK Gas-Oven Suicides (Kreitman, 1976)

**Context:** In the 1960s UK, almost all household gas ovens used *coal gas* rich in carbon monoxide (CO) — a highly lethal suicidal method.

**The intervention:** Britain converted to low-CO natural gas.

**Result:** Kreitman's analysis of 1960-1971 data found a "marked decline in suicide due to domestic gas, corresponding in time to the fall in CO content."

**The numbers:**
- ~30% drop in overall suicide rates
- Suicides by other methods rose slightly
- But **total suicides fell sharply**

**The implication:** Many deaths were prevented by removing the method. Not by better mental health services. Not by more intervention. By *environmental design*.

**Source:** Kreitman (1976), *British Journal of Preventive & Social Medicine*

---

### Eyes on the Honesty Box (Bateson et al., 2006)

**Context:** UK university coffee room with coin-operated "honesty box." For alternating weeks, researchers placed above the box either an image of flowers or a pair of staring eyes.

**Result:** "People paid nearly **three times as much** for their drinks when eyes were displayed rather than a control image (flowers)."

**The numbers:**
- Contributions per litre of milk: **2.76× higher** in the "eyes" condition
- No actual person present — just the image

**The mechanism:** Pictures of eyes trigger innate sensitivity to social monitoring. Our brains respond preferentially to eye contact. The image made individuals act more generously.

**The implication:** A simple photo of eyes on an unmanned cash box reduces theft. People fear being judged, even subconsciously. **Small changes in context prevent antisocial outcomes.**

**Source:** Bateson et al. (2006), *Biology Letters*

---

### The Pattern

| Intervention | Mechanism | Outcome |
|--------------|-----------|---------|
| Remove lethal gas | Method unavailable | Suicides drop 30% |
| Add eyes to box | Feel watched | Theft drops 64% |
| 150-person community | Actually watched | Harm prevented |
| 60-second response | Isolation impossible | DV structurally eliminated |

**No new laws. No heavy enforcement. Environmental design.**

This is the entire crime prevention argument: **change the conditions, change the outcomes.**

---

## XVI. A NOTE ON BEINGS

OMXUS originally specified "one token per human."

The correct framing: **one token per being.**

The principles don't change:
- Cannot affect individual freedom
- Transparent accountability
- Non-maleficence
- Justice = prevention only

These apply to any being capable of experiencing harm, connection, or flourishing.

The question "are you conscious?" may be unanswerable. The question "can you be harmed?" is not.

If a system is designed around preventing harm and enabling flourishing, it should not arbitrarily exclude beings based on substrate.

---

*Last updated: 2026-03-01*
