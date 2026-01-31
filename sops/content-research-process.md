# SOP: Content Research Process

## Purpose
Conduct thorough research before creating any marketing content to ensure messaging resonates with target audience, addresses real pain points, and differentiates from competitors.

## When to Use
- Before writing email sequences
- Before creating landing pages
- Before launching campaigns
- When entering new market segments
- When positioning shifts

---

## Research Framework: The 4 Ps

1. **Pain Points** - What problems does the audience face?
2. **Positioning** - How do competitors address these problems?
3. **Proof Points** - What evidence do we have that our solution works?
4. **Persona** - Who exactly are we talking to?

---

## Phase 1: Audience Research

### 1.1 Define the Persona

**Demographics**:
- [ ] Job title(s)
- [ ] Company size (employees, revenue)
- [ ] Industry/vertical
- [ ] Geographic location
- [ ] Tech stack (if relevant)

**Psychographics**:
- [ ] What keeps them up at night?
- [ ] What are their goals/KPIs?
- [ ] What are their daily frustrations?
- [ ] How do they measure success?
- [ ] What's their decision-making process?

**Claude Code Command**: `/research-persona [job-title]`

**Output**: Save to `/examples/research/persona-[name].md`

---

### 1.2 Pain Point Discovery

**Methods**:

**A. Review Site Research**
- G2
- Capterra
- TrustRadius
- Reddit (search: "r/[industry] + [problem]")
- Quora

**What to look for**:
- Complaints about existing solutions
- Feature requests
- Common frustrations
- Workarounds people use

**Questions to answer**:
- What are the top 5 complaints about [competitor]?
- What features do people wish existed?
- What's the most common frustration?
- What do they say they "love" or "hate"?

---

**B. Social Media Listening**
- LinkedIn (search for job title + problem keywords)
- Twitter/X (search for #[industry] + pain point keywords)
- Industry-specific Slack/Discord communities

**What to look for**:
- Questions people are asking
- Complaints or venting
- Advice requests
- Tool recommendations

**Save quotes** that capture pain points in their own words.

---

**C. Customer Interview Mining**
(If you have access to existing customer data)

- Review sales call transcripts
- Read support tickets
- Analyze onboarding feedback
- Check NPS survey responses

**Questions to answer**:
- What problem were they trying to solve when they found us?
- What was their "aha moment"?
- What almost made them not buy?
- How do they describe the product to others?

---

**D. Search Behavior Analysis**

Use tools:
- Google Keyword Planner
- AnswerThePublic
- AlsoAsked
- Reddit/Quora search

**Queries to research**:
- "[problem] solution"
- "how to [solve problem]"
- "[competitor] alternative"
- "[industry] tools"

**What to capture**:
- High-volume search terms (their language, not yours)
- Questions they're asking
- Comparison searches

---

**Output**: Pain Points Document

Create: `/examples/research/pain-points-[audience].md`

```markdown
# Pain Points: [Audience Name]

## Top 5 Pain Points (Prioritized)

### 1. [Pain Point Name]
**Description**: [What is the problem]
**Impact**: [Why it matters / cost of not solving]
**Frequency**: [How often mentioned]
**Evidence**: [Quotes, data, sources]
**Current Solutions**: [What they do now / workarounds]

[Repeat for all 5]

## Quotes (In Their Own Words)
- "[Customer quote showing pain]" - Source: [G2 review, Reddit, etc.]
- "[Another quote]" - Source: [...]

## Search Queries
- "[problem] solution" - 2,400 searches/mo
- "how to [solve problem]" - 1,800 searches/mo
```

---

## Phase 2: Competitor Research

### 2.1 Identify Competitors

**Direct Competitors**: Same solution, same audience
**Indirect Competitors**: Different solution, same problem
**Substitutes**: What do people do if they don't use any tool?

**Claude Code Command**: `/research-competitors [industry]`

---

### 2.2 Analyze Messaging

**For each competitor, capture**:

**Homepage**:
- [ ] Headline
- [ ] Subheadline
- [ ] Value proposition
- [ ] Target audience called out?
- [ ] Primary CTA

**Positioning**:
- [ ] What pain point do they lead with?
- [ ] What benefit do they promise?
- [ ] How do they differentiate?
- [ ] What proof do they show?

**Tone/Voice**:
- [ ] Professional or casual?
- [ ] Jargon-heavy or plain language?
- [ ] Feature-focused or benefit-focused?

**Email Examples** (if available):
- Sign up for their trials
- Analyze email sequences
- Note timing, subject lines, CTAs

---

**Positioning Map Template**:

Create: `/examples/research/competitor-analysis-[date].md`

```markdown
# Competitor Analysis: [Industry/Category]

## Competitor Matrix

| Competitor | Headline | Primary Pain Point | Differentiation | Target Audience | Pricing |
|------------|----------|-------------------|-----------------|-----------------|---------|
| [Name] | [Headline] | [Pain] | [How they differentiate] | [Who they target] | [$X/mo] |
| [Name] | [...] | [...] | [...] | [...] | [...] |

## Messaging Patterns

**Common themes across competitors**:
- [Pattern 1]
- [Pattern 2]
- [Pattern 3]

**Gaps we can exploit**:
- [Opportunity 1: What no one is saying]
- [Opportunity 2: Underserved audience segment]
- [Opportunity 3: Pain point being ignored]

## Voice/Tone Analysis
- [X competitors] use corporate/formal tone
- [Y competitors] use casual/conversational tone
- [Z competitors] use technical/developer-focused language

**Our opportunity**: [How we can stand out]

## Email Sequence Analysis

### [Competitor Name]
- Email 1: [Subject, angle, CTA]
- Email 2: [Subject, angle, CTA]
- Email 3: [Subject, angle, CTA]

**What works**: [Takeaways]
**What doesn't**: [Gaps]
```

---

## Phase 3: Proof Point Collection

### 3.1 Gather Internal Data

**Customer Success Metrics**:
- [ ] Average improvement (%, time saved, $ saved)
- [ ] Time to value (how quickly they see results)
- [ ] ROI data (if available)
- [ ] Usage statistics (engagement, retention)

**Case Studies/Testimonials**:
- [ ] Customer name + title (if permission granted)
- [ ] Specific problem they had
- [ ] Specific result they achieved
- [ ] Quote in their own words

**Product Data**:
- [ ] Number of customers
- [ ] Number of users
- [ ] Volume processed (emails sent, projects managed, etc.)
- [ ] Uptime/reliability stats

---

### 3.2 Social Proof Inventory

**Review Sites**:
- G2 rating + number of reviews
- Capterra rating + number of reviews
- Best quotes from reviews

**Media Mentions**:
- Press coverage
- Industry awards
- Analyst reports (Gartner, Forrester, etc.)

**Notable Customers**:
- Logos (if permission granted)
- Company names to drop (if allowed)

---

**Output**: Proof Points Library

Create: `/examples/research/proof-points.md`

```markdown
# Proof Points Library

## Metrics
- [X] customers using the product
- [Y%] average improvement in [metric]
- [Z] hours saved per week on average
- [$X] average ROI in first 90 days

## Customer Success Stories

### [Company Name] - [Industry]
**Problem**: [What they struggled with]
**Solution**: [How we helped]
**Result**: [Specific metric - X% improvement in Y]
**Quote**: "[Testimonial in their words]" - Name, Title

[Repeat for 5-10 stories]

## Social Proof
- ⭐ 4.8/5 on G2 (200+ reviews)
- 🏆 "Best [Category] Software 2024" - [Publication]
- 📰 Featured in [TechCrunch, Forbes, etc.]

## Notable Customer Logos
[List of companies we can name-drop]
```

---

## Phase 4: Message Development

### 4.1 Create Messaging Hierarchy

Based on research, build messaging framework:

```markdown
# Messaging Framework: [Product/Campaign Name]

## Target Audience
[Primary persona] at [company type]

## Core Message (One Sentence)
[What we do] for [who] so they can [benefit]

## Key Pain Points (Prioritized)
1. [Most urgent pain]
2. [Second most urgent]
3. [Third most urgent]

## Value Propositions (By Pain Point)

### Pain Point 1: [Name]
**Promise**: [What we deliver]
**Proof**: [Metric or testimonial]
**Differentiator**: [Why we're better than alternatives]

[Repeat for each pain point]

## Positioning Statement
For [target audience] who [pain point], [Product Name] is a [category] that [key benefit]. Unlike [competitors], we [unique differentiator].

## Supporting Messages
- [Benefit 1 with proof point]
- [Benefit 2 with proof point]
- [Benefit 3 with proof point]

## Objections & Responses
- **Objection**: "[Common concern]"
  **Response**: [How we address it + proof]

[Repeat for 3-5 objections]
```

---

### 4.2 Test Messaging

**A/B Test Ideas**:
- Which pain point resonates most?
- Which proof point is most compelling?
- Which CTA gets most clicks?

**Methods**:
- Email subject line tests
- Landing page headline tests
- Ad copy variations

**Track**:
- Open rates (subject line effectiveness)
- Click rates (body copy effectiveness)
- Conversion rates (overall message fit)

---

## Phase 5: Documentation & Sharing

### 5.1 Create Research Brief

**Output**: `/examples/research/brief-[campaign-name].md`

```markdown
# Research Brief: [Campaign Name]

## Executive Summary
[2-3 paragraphs summarizing key findings]

## Target Audience
[Persona summary]

## Key Insights
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]

## Recommended Messaging
**Headline**: [Recommended headline]
**Key Messages**: [3-5 key messages to communicate]
**Proof Points**: [Which stats/testimonials to feature]
**Differentiators**: [How to position against competitors]

## Content Recommendations
- Email sequence: [Angle to take]
- Landing page: [Structure and focus]
- Ads: [Hook to use]

## Appendix
- Full pain points: [Link to doc]
- Competitor analysis: [Link to doc]
- Proof points: [Link to doc]
```

---

### 5.2 Share with Team

- Save all research to `/examples/research/`
- Update CLAUDE.md with key insights (if ongoing)
- Brief copywriters/designers
- Create template for this persona (if new)

---

## Tools & Resources

**Research Tools**:
- G2, Capterra, TrustRadius (reviews)
- AnswerThePublic (search behavior)
- Reddit, Quora (voice of customer)
- SparkToro (audience research)
- SimilarWeb (competitor traffic analysis)

**Claude Code Commands**:
- `/research-persona [title]` - Deep dive on persona
- `/research-competitors [industry]` - Competitor analysis
- `/research-topic [keyword]` - Content ideation

**Templates**:
- Pain points template
- Competitor analysis template
- Messaging framework template

---

## Quality Checklist

Before considering research "complete":

- [ ] Identified 5+ specific pain points with evidence
- [ ] Analyzed 3+ direct competitors
- [ ] Collected 5+ customer proof points (metrics, quotes)
- [ ] Created messaging hierarchy
- [ ] Documented findings in research brief
- [ ] Shared with team/stakeholders

---

## Revision History
- v1.0 - Initial research process documented
