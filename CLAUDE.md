# Claude Code Course - Project Instructions

## Project Overview

This is a learning environment for mastering Claude Code for copywriting, marketing campaigns, and content creation. This project demonstrates how to leverage agents, skills, and automation scripts for non-coding workflows.

## Purpose

Train users to use Claude Code for:
- Writing conversion-focused copy
- Managing email campaigns via Smartlead
- Automating repetitive marketing tasks
- Maintaining brand voice consistency
- Creating repeatable workflows

---

## Project Structure

```
CCCfolder/
├── .claude/
│   ├── agents/              # Specialized AI agents for specific tasks
│   │   ├── copywriter-agent.md
│   │   ├── campaign-creator.md
│   │   └── content-researcher.md
│   ├── skills/              # Custom slash commands
│   │   ├── email-sequence/
│   │   ├── improve-copy/
│   │   └── launch-campaign/
│   └── settings.json        # Claude Code configuration
├── scripts/                 # Python automation scripts
│   └── [Smartlead API scripts]
├── templates/               # Reusable copy templates
│   ├── cold-email-template.md
│   ├── nurture-sequence-template.md
│   └── landing-page-copy-template.md
├── examples/                # Real session examples
│   ├── email-sequence-example.md
│   ├── campaign-launch-workflow.md
│   └── copy-improvement-session.md
├── sops/                    # Standard operating procedures
│   ├── campaign-launch-checklist.md
│   ├── brand-voice-guidelines.md
│   └── content-research-process.md
└── CLAUDE.md               # This file
```

---

## How to Use This Project

### For Copywriting Tasks

1. **Check brand voice first**: Always review `/sops/brand-voice-guidelines.md`
2. **Use templates**: Start with templates in `/templates/` folder
3. **Invoke skills**:
   - `/email-sequence [number]` - Create email sequences
   - `/improve-copy` - Polish existing content
4. **Use agents**: Claude will automatically delegate to specialized agents based on task

### For Campaign Management

1. **Follow checklist**: Use `/sops/campaign-launch-checklist.md`
2. **Prepare leads**: Clean and validate lead lists
3. **Create campaign**: Claude will invoke campaign-creator agent
4. **Launch**: Use `/launch-campaign [name]` to go live
5. **Monitor**: Check metrics 24-48 hours after launch

### For Research

1. **Use research process**: Follow `/sops/content-research-process.md`
2. **Invoke research agent**: Claude will use content-researcher agent for deep dives
3. **Save findings**: Store research in `/examples/research/`

---

## Brand Voice Guidelines

### Core Principles

**Voice Attributes**:
1. **Conversational, Not Corporate** - Write like you talk, use contractions
2. **Confident, Not Arrogant** - State facts with proof, avoid superlatives
3. **Helpful, Not Pushy** - Lead with value, respect decisions
4. **Clear, Not Clever** - Get to the point, use simple words
5. **Human, Not Robotic** - Show personality, admit mistakes

See full guidelines: `/sops/brand-voice-guidelines.md`

### Quick Reference

**Use These Words**:
- You, your (reader-focused)
- Specific metrics (40% reduction, not "significant improvement")
- Because (reason-why)
- Proven, results, easy

**Avoid These**:
- ❌ Synergy, leverage, paradigm shift
- ❌ Revolutionary, game-changer (without proof)
- ❌ Best, ultimate, #1 (without data)
- ❌ All caps, excessive punctuation!!!

---

## Copywriting Frameworks

### PAS (Problem-Agitate-Solution)
1. **Problem**: State the pain point
2. **Agitate**: Make them feel the cost of not solving it
3. **Solution**: Present your solution as the fix

### AIDA (Attention-Interest-Desire-Action)
1. **Attention**: Hook with bold statement or question
2. **Interest**: Build engagement with relevant details
3. **Desire**: Show benefits and proof
4. **Action**: Clear CTA

### BAB (Before-After-Bridge)
1. **Before**: Life with the problem
2. **After**: Life with the solution
3. **Bridge**: How to get from before to after

---

## Campaign Requirements

### Email Campaigns

**Deliverability Checklist**:
- ✅ Domain warmed up (2+ months old)
- ✅ SPF, DKIM, DMARC configured
- ✅ Lead list validated
- ✅ Daily sending limits set appropriately
- ✅ Unsubscribe link included
- ✅ Test email sent and checked

**Best Practices**:
- Keep emails under 150 words
- One clear CTA per email
- Personalize first line with research
- A/B test subject lines
- Send Tuesday-Thursday, 8-10am recipient timezone

**Success Metrics**:
- Open rate: >40% (excellent), >35% (good)
- Reply rate: >5% (excellent), >3% (good)
- Bounce rate: <2%
- Spam complaints: <0.1%

---

## Automation Scripts

### Available Scripts (in `/scripts/`)

**Campaign Management**:
- `create-campaign.py` - Create new campaign in Smartlead
- `add-leads.py` - Upload and validate leads
- `configure-campaign.py` - Set sending settings
- `activate-campaign.py` - Launch campaign
- `pause-campaign.py` - Emergency stop

**Usage**:
Claude Code will automatically execute these scripts when you use relevant skills or agents. You don't need to run them manually.

---

## Agent Behavior

### When Claude Uses Agents

Claude will automatically delegate to specialized agents for:

1. **copywriter-agent**: Writing email sequences, ads, landing page copy
2. **campaign-creator**: Setting up and managing Smartlead campaigns
3. **content-researcher**: Researching topics, competitors, audience insights

You can also explicitly invoke: "Use the copywriter agent to create..."

### Agent Instructions

Agents follow these guidelines:
- Always check CLAUDE.md for brand voice
- Use templates when available
- Save outputs to appropriate folders
- Ask clarifying questions before starting
- Provide A/B test variations

---

## File Organization

### Where to Save Things

**Research**: `/examples/research/`
- persona-[name].md
- pain-points-[audience].md
- competitor-analysis-[date].md
- brief-[campaign-name].md

**Campaign Docs**: `/examples/campaigns/`
- [campaign-name]-[date].md
- Include: setup, metrics, learnings

**Copy Drafts**: `/templates/`
- Use descriptive names
- Include version numbers if iterating
- Add notes about what works/doesn't

---

## Learning Path

### Week 1: Basics
- Understand agents, skills, and commands
- Write first email sequence using `/email-sequence`
- Improve existing copy using `/improve-copy`
- Review brand voice guidelines

### Week 2: Campaigns
- Set up first Smartlead campaign
- Follow campaign launch checklist
- Monitor and optimize based on metrics
- Learn from examples in `/examples/`

### Week 3: Automation
- Understand Python scripts in `/scripts/`
- Create custom skills for your workflows
- Build repeatable processes
- Document SOPs for your team

### Week 4: Advanced
- Create custom agents for your use cases
- Build A/B testing workflows
- Integrate with other tools
- Share best practices

---

## Common Workflows

### 1. Cold Email Sequence Creation

```
User: "Create a 3-email cold outreach sequence for [audience]"
→ Claude researches pain points
→ Uses copywriter-agent to draft sequence
→ Applies brand voice guidelines
→ Provides A/B test variations
→ Saves to /templates/
```

### 2. Campaign Launch

```
User: "/launch-campaign [name]"
→ Runs pre-launch checklist
→ Validates lead list
→ Configures settings
→ Sends test email
→ Activates campaign
→ Sets up monitoring
```

### 3. Copy Improvement

```
User: "/improve-copy [paste copy]"
→ Analyzes against brand voice
→ Identifies weak points
→ Provides improved version
→ Explains changes
→ Suggests A/B tests
```

---

## Important Notes

### Before Every Copywriting Task:
1. ✅ Read brand voice guidelines (`/sops/brand-voice-guidelines.md`)
2. ✅ Check if template exists (`/templates/`)
3. ✅ Review past examples (`/examples/`)
4. ✅ Understand target audience and pain points

### Before Launching Campaigns:
1. ✅ Complete campaign launch checklist (`/sops/campaign-launch-checklist.md`)
2. ✅ Validate all lead emails
3. ✅ Send test email
4. ✅ Verify deliverability settings
5. ✅ Set up monitoring alerts

### After Campaign Launch:
1. ✅ Check metrics after 24 hours
2. ✅ Monitor deliverability (bounce rate, spam complaints)
3. ✅ Document learnings in `/examples/campaigns/`
4. ✅ Iterate based on data

---

## Tips for Success

**Claude Code Best Practices**:
- Use skills for repetitive tasks
- Create agents for specialized workflows
- Document everything in examples/
- Build SOPs for team consistency
- Iterate based on results

**Copywriting Best Practices**:
- Always start with research
- Lead with benefits, not features
- Use specific numbers and proof
- Keep it conversational
- Test everything

**Campaign Best Practices**:
- Warm up domains properly
- Start with conservative sending limits
- Monitor deliverability closely
- A/B test systematically
- Learn from each campaign

---

## Getting Help

**Within Claude Code**:
- Ask Claude: "How do I [task]?"
- Check examples: `/examples/`
- Review SOPs: `/sops/`
- Read templates: `/templates/`

**Resources**:
- Brand Voice: `/sops/brand-voice-guidelines.md`
- Campaign Checklist: `/sops/campaign-launch-checklist.md`
- Research Process: `/sops/content-research-process.md`

---

## Quick Reference Commands

**Skills**:
- `/email-sequence [number]` - Create email sequence
- `/improve-copy` - Improve existing copy
- `/launch-campaign [name]` - Launch campaign (manual)

**Agents** (auto-invoked):
- copywriter-agent - Conversion-focused writing
- campaign-creator - Smartlead campaign setup
- content-researcher - Research and insights

---

## Revision History
- v1.0 - Initial course setup
- Focus: Copywriting, campaigns, Smartlead integration
