# SOP: Campaign Launch Checklist

## Purpose
Ensure every email campaign is properly configured, tested, and optimized before going live to protect domain reputation and maximize results.

## When to Use
Before activating any new email campaign in Smartlead.

---

## Phase 1: Pre-Launch Setup (Day -3 to -1)

### 1. Campaign Strategy ✅
- [ ] **Campaign objective defined**
  - What's the goal? (demos booked, calls scheduled, downloads, etc.)
  - What's the success metric?
  - What's the target conversion rate?

- [ ] **Target audience documented**
  - ICP (Ideal Customer Profile) defined
  - Lead list sourced and segmented
  - Personalization data available (name, company, title, etc.)

- [ ] **Campaign timeline planned**
  - Start date set
  - Expected completion date
  - Follow-up campaign planned (if needed)

### 2. Copy & Content ✅
- [ ] **Email sequence written**
  - All emails drafted (3-5 emails recommended)
  - Each email can stand alone (not everyone reads previous)
  - Brand voice matches CLAUDE.md guidelines
  - Mobile-friendly (short paragraphs, clear CTA)

- [ ] **Subject lines created**
  - 3 variations per email for A/B testing
  - Under 50 characters (mobile optimization)
  - No spam trigger words ("free", "guarantee", "act now")
  - Personalization tokens included where relevant

- [ ] **CTAs optimized**
  - One clear CTA per email
  - Action-oriented language
  - Low-friction ask (15-min call, not "buy now")

- [ ] **Personalization tokens verified**
  - All tokens have fallback values
  - Tested with sample data
  - Custom fields mapped correctly

### 3. Lead List Preparation ✅
- [ ] **List cleaned and validated**
  - Emails validated (catch-all, invalid, syntax errors removed)
  - Duplicates removed
  - Bounced emails from previous campaigns excluded
  - Unsubscribes removed

- [ ] **Data enriched**
  - First name, last name present
  - Company name available
  - Job title/role included
  - Custom personalization data added

- [ ] **Segmentation applied**
  - Lists segmented by company size, industry, or behavior
  - Separate campaigns for different segments (if needed)
  - Tags applied for tracking

- [ ] **CSV formatted correctly**
  - Headers match Smartlead requirements
  - Special characters encoded properly
  - File size under limit

### 4. Domain & Deliverability ✅
- [ ] **Sending domain warmed up**
  - Domain age: 2+ months minimum
  - Warmup period completed (gradual volume increase)
  - Domain reputation checked (MXToolbox, Google Postmaster)

- [ ] **SPF, DKIM, DMARC configured**
  - SPF record includes Smartlead
  - DKIM signature active
  - DMARC policy set (p=none or p=quarantine)

- [ ] **Sender reputation healthy**
  - No blacklisting (check SpamHaus, Barracuda)
  - Complaint rate <0.1%
  - Bounce rate <2%

- [ ] **Daily sending limits set**
  - New domain (<3 months): 20-50/day
  - Warmed domain (3-6 months): 50-100/day
  - Aged domain (6+ months): 100-200/day

---

## Phase 2: Campaign Configuration (Day -1)

### 5. Smartlead Setup ✅
- [ ] **Campaign created in Smartlead**
  - Naming convention followed: `[Client]-[Audience]-[Month]-[Year]`
  - Example: `Acme-SaaS-CTOs-Jan-2024`

- [ ] **Email sequence uploaded**
  - All emails added in correct order
  - Timing between emails set (2-4 days recommended)
  - Stop sending if reply received (enabled)

- [ ] **Sending schedule configured**
  - Time zone detection enabled
  - Sending window: 8am-5pm recipient local time
  - Best days: Tuesday-Thursday
  - Avoid Mondays (inbox overload) and Fridays (weekend mode)

- [ ] **Tracking enabled**
  - Link tracking ON
  - Open tracking ON
  - Reply detection ON
  - Unsubscribe link included (legally required)

- [ ] **Settings optimized**
  - Email delay randomized (avoid spam patterns)
  - "Sent from" name personalized
  - Reply-to address monitored inbox

### 6. Lead Upload ✅
- [ ] **Leads imported to Smartlead**
  - CSV uploaded without errors
  - All columns mapped correctly
  - Lead count matches expectation

- [ ] **Custom fields verified**
  - Personalization tokens pulling correct data
  - Fallback values working
  - Preview shows proper formatting

---

## Phase 3: Testing (Day -1 to Launch Day)

### 7. Test Sends ✅
- [ ] **Internal test email sent**
  - Sent to team email addresses
  - Check: Personalization tokens filled
  - Check: Links work and track correctly
  - Check: Images load properly
  - Check: Mobile rendering looks good
  - Check: Lands in inbox (not spam/promotions)

- [ ] **Spam score checked**
  - Run through Mail-Tester.com (score 8+/10)
  - Run through Litmus or Email on Acid
  - No spam trigger words flagged

- [ ] **Deliverability test**
  - Send to Gmail, Outlook, Apple Mail
  - Verify inbox placement
  - Check spam folder

- [ ] **Edge cases tested**
  - Missing first name (fallback works)
  - Missing company (fallback works)
  - Long names (formatting OK)

### 8. Final Review ✅
- [ ] **Copy proofread**
  - No typos or grammatical errors
  - Links go to correct destinations
  - Sender name and email correct
  - Unsubscribe link present and functional

- [ ] **Legal compliance**
  - CAN-SPAM compliant (US)
  - GDPR compliant (EU) - if applicable
  - Physical address included (if required)
  - Unsubscribe honored within 10 days

- [ ] **Stakeholder approval**
  - Client/manager approved final copy
  - Marketing team signed off
  - Legal reviewed (if needed)

---

## Phase 4: Launch (Launch Day)

### 9. Activation ✅
- [ ] **Campaign activated in Smartlead**
  - Double-check campaign name
  - Verify lead count
  - Confirm schedule settings
  - Enable campaign

- [ ] **Monitoring set up**
  - Deliverability alerts configured
    - Bounce rate >2% = alert
    - Spam complaints >0.1% = alert
    - Unsubscribe rate >1% = alert
  - Dashboard bookmarked
  - Reply inbox monitored

- [ ] **Documentation updated**
  - Campaign details saved to `/examples/campaigns/[name].md`
  - Tracking spreadsheet updated
  - Team notified campaign is live

---

## Phase 5: Post-Launch Monitoring (First 48 Hours)

### 10. Initial Metrics Review ✅
**After 24 hours**, check:
- [ ] **Deliverability health**
  - Bounce rate <2% ✅
  - No spam complaints ✅
  - Domain reputation stable ✅

- [ ] **Engagement metrics**
  - Open rate (target: 35-50%)
  - Click rate (target: 5-15%)
  - Reply rate (target: 2-5%)

- [ ] **Quality signals**
  - Are replies positive/negative/interested?
  - Any complaints or unsubscribe feedback?
  - Are the right people responding?

**After 48 hours**, decide:
- [ ] Continue as-is (if metrics are good)
- [ ] Adjust copy (if open rate low)
- [ ] Pause campaign (if deliverability issues)
- [ ] Segment differently (if wrong audience responding)

---

## Emergency Procedures

### If Bounce Rate >5%
1. **PAUSE CAMPAIGN IMMEDIATELY**
2. Check lead list quality
3. Run email validation
4. Remove invalid emails
5. Reduce daily send volume
6. Resume with caution

### If Spam Complaints >0.3%
1. **PAUSE CAMPAIGN IMMEDIATELY**
2. Review copy for spam triggers
3. Check list source (was it opted-in?)
4. Ensure unsubscribe link works
5. Contact Smartlead support
6. Do NOT resume until issue resolved

### If Blacklisted
1. **STOP ALL SENDING**
2. Check blacklist (SpamHaus, Barracuda, etc.)
3. Request delisting (if legitimate)
4. Investigate root cause
5. Implement fix before resuming
6. Consider using different domain

---

## Success Criteria

### Excellent Campaign
- ✅ Bounce rate: <1%
- ✅ Open rate: >45%
- ✅ Reply rate: >5%
- ✅ Positive reply rate: >50% of replies
- ✅ Meeting booked rate: >2%
- ✅ Spam complaints: 0

### Good Campaign
- ✅ Bounce rate: 1-2%
- ✅ Open rate: 35-45%
- ✅ Reply rate: 3-5%
- ✅ Positive reply rate: >30% of replies
- ✅ Meeting booked rate: >1%
- ✅ Spam complaints: <0.1%

### Needs Improvement
- ⚠️ Bounce rate: 2-5%
- ⚠️ Open rate: 25-35%
- ⚠️ Reply rate: 1-3%
- ⚠️ Positive reply rate: <30% of replies
- ⚠️ Meeting booked rate: <1%

### STOP and Fix
- 🛑 Bounce rate: >5%
- 🛑 Open rate: <25%
- 🛑 Reply rate: <1%
- 🛑 Spam complaints: >0.3%

---

## Tools & Resources
- **Email validation**: ZeroBounce, NeverBounce
- **Spam testing**: Mail-Tester.com, Litmus
- **Deliverability**: Google Postmaster Tools, MXToolbox
- **Copy templates**: `/templates/`
- **Past campaigns**: `/examples/campaigns/`

## Revision History
- v1.0 - Initial SOP created
