# Example: Complete Campaign Launch Workflow

## Scenario
Launching a cold outreach campaign for 500 leads targeting B2B SaaS CTOs.

## Full Claude Code Session

### Step 1: Campaign Setup

**User**: "Set up a new Smartlead campaign called 'SaaS-CTO-Q1-2024'"

**Claude**: I'll help set up your campaign. Let me gather the details:

1. Campaign objective? (meetings booked, demo requests, etc.)
2. Email sequence ready? (Or should I help create it?)
3. Lead list prepared? (CSV format required)
4. Sending domain? (Must be warmed up)

**User**:
- Objective: Book 15-minute discovery calls
- Use the sequence from /templates/sequences/saas-churn-reduction.md
- Lead list at /data/saas-cto-leads-500.csv
- Domain: outreach@mycompany.io (warmed up, 2 months old)

---

### Step 2: Create Campaign

**Claude invokes**: Campaign Creator Agent

**Claude executes**:
```bash
python scripts/create-campaign.py \
  --name "SaaS-CTO-Q1-2024" \
  --from-email "outreach@mycompany.io" \
  --from-name "Sarah Chen" \
  --sequence-file "templates/sequences/saas-churn-reduction.md"
```

**Output**:
```
✓ Campaign created successfully
✓ Campaign ID: camp_abc123
✓ 3 emails configured
✓ Dashboard: https://app.smartlead.ai/campaigns/camp_abc123
```

---

### Step 3: Lead Upload & Validation

**Claude**: Campaign created! Now uploading and validating your leads...

**Claude executes**:
```bash
python scripts/add-leads.py \
  --campaign-id "camp_abc123" \
  --lead-file "data/saas-cto-leads-500.csv" \
  --validate-emails
```

**Output**:
```
Validating 500 leads...
✓ 478 valid emails
✗ 22 invalid/duplicate emails removed

Segmentation detected:
- 200 leads: Series A-B companies
- 178 leads: Series C+ companies
- 100 leads: Bootstrapped

Upload complete!
```

**Claude**: I noticed your leads fall into 3 segments. Want to create separate campaigns for better personalization? Series A/B companies have different pain points than Series C+.

**User**: Good catch, but let's keep it simple for now. Just use the single campaign.

---

### Step 4: Configure Sending Settings

**Claude**: Configuring optimal sending settings for a 2-month-old domain...

**Recommended settings**:
- Daily limit: 50 emails/day (conservative for domain age)
- Sending window: 8am-5pm recipient timezone
- Days: Tuesday-Thursday (best response rates)
- Ramp schedule: +10 emails/day per week until 100/day

**Claude**: Should I apply these settings?

**User**: Yes, but increase to 60/day. We've had good deliverability.

**Claude executes**:
```bash
python scripts/configure-campaign.py \
  --campaign-id "camp_abc123" \
  --daily-limit 60 \
  --time-window "8-17" \
  --days "tue,wed,thu" \
  --enable-timezone-detection
```

**Output**: ✓ Settings applied

---

### Step 5: Test Send

**Claude**: Before going live, sending test email to verify everything works...

**Claude executes**:
```bash
python scripts/send-test-email.py \
  --campaign-id "camp_abc123" \
  --test-email "sarah@mycompany.io"
```

**Claude**: Check your inbox for test email. Verify:
- [ ] Personalization tokens filled correctly
- [ ] Links track properly
- [ ] Images load
- [ ] Unsubscribe link works
- [ ] Lands in inbox (not spam)

**User**: ✅ Looks good!

---

### Step 6: Final Launch

**Claude**: Ready to launch! This will activate the campaign and start sending according to the schedule.

**User**: `/launch-campaign SaaS-CTO-Q1-2024`

**Claude executes**:
```bash
python scripts/activate-campaign.py --campaign-id "camp_abc123"
```

**Output**:
```
🚀 Campaign Activated!

Campaign: SaaS-CTO-Q1-2024
Status: Active
Leads: 478
Daily sends: 60
Est. completion: 8 days

Dashboard: https://app.smartlead.ai/campaigns/camp_abc123

Monitoring:
- Deliverability alerts enabled
- Reply detection active
- Bounce rate monitoring set (alert if >2%)
```

---

### Step 7: Post-Launch Monitoring

**Claude**: Campaign is live! I've set up:

1. **24-hour check-in**: Tomorrow at this time, I'll pull initial metrics
2. **Alerts configured**:
   - Bounce rate >2%
   - Spam complaints
   - Domain blacklisting
   - Unsubscribe rate >1%

3. **Success metrics to track**:
   - Open rate (target: >40%)
   - Reply rate (target: >5%)
   - Meeting booked rate (target: >2%)

I'll save this campaign info to `/examples/campaigns/saas-cto-q1-2024.md` for reference.

Want me to create a follow-up task to review results in 24 hours?

**User**: Yes please

**Claude creates reminder**: ✓ Task created: Review SaaS-CTO campaign results (due: tomorrow)

---

## Campaign Results (24 Hours Later)

**Claude** (automated check-in): Here are your first 24-hour results:

```
Campaign: SaaS-CTO-Q1-2024
Emails sent: 60
Opens: 28 (46.7%) ✅ Above target
Clicks: 8 (13.3%)
Replies: 3 (5.0%) ✅ On target
Meetings booked: 1 (1.7%)
Bounces: 0 (0%) ✅
Spam: 0 (0%) ✅

Deliverability: Excellent
Domain reputation: Good
```

**Analysis**: Strong start! Open and reply rates are hitting targets. Consider:
- Email 2 will go out tomorrow to non-responders
- Watch reply sentiment (I can help with response templates)
- If patterns emerge, we can adjust Email 3 before it sends

---

## Key Lessons
- Thorough setup prevents issues
- Test sends catch problems early
- Conservative sending limits protect domain
- Monitoring catches problems before they escalate
- Segmentation suggestion showed proactive thinking
