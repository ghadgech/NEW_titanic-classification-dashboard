import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="AI Strategic Foundations",
    page_icon="🤖",
    layout="wide",
)

# ──────────────────────────────────────────────
# STYLES
# ──────────────────────────────────────────────

st.markdown("""
<style>
.module-card {
    background: linear-gradient(135deg, #1e3a5f 0%, #0d2137 100%);
    border-radius: 12px;
    padding: 20px;
    margin: 8px 0;
    border-left: 4px solid #4fc3f7;
    color: white;
}
.concept-pill {
    display: inline-block;
    background: #1565c0;
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    margin: 4px 3px;
    font-size: 0.85em;
}
.highlight-box {
    background: #e3f2fd;
    border-left: 4px solid #1976d2;
    padding: 12px 16px;
    border-radius: 4px;
    margin: 10px 0;
    color: #0d47a1;
}
.kpi-number {
    font-size: 2.2em;
    font-weight: bold;
    color: #1976d2;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ──────────────────────────────────────────────

MODULES = [
    "🏠 Overview",
    "🎯 AI Strategic Foundations",
    "🤖 AI Agents & Autonomous Systems",
    "✨ Generative AI for Service Delivery",
    "⚖️ AI Governance, Ethics & Risk",
    "📋 ISO 42001",
    "💼 AI-driven Client Experience & Service Quality",
    "🚀 Leading AI Adoption in Delivery Teams",
]

st.sidebar.title("AI Strategic Foundations")
st.sidebar.markdown("---")
selected = st.sidebar.radio("Navigate", MODULES, label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.caption("AI Capability Framework · 2025")


# ──────────────────────────────────────────────
# OVERVIEW
# ──────────────────────────────────────────────

if selected == "🏠 Overview":
    st.title("AI Strategic Foundations")
    st.markdown("### Your end-to-end guide to leading AI in the enterprise")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Modules", "7", "Core Topics")
    with col2:
        st.metric("Frameworks", "12+", "Industry Standards")
    with col3:
        st.metric("Use Cases", "40+", "Practical Examples")
    with col4:
        st.metric("Standard", "ISO 42001", "AI Governance")

    st.markdown("---")

    # ── Chart 1: Programme Sunburst ──────────────────────────────────────
    st.markdown("### Programme at a Glance")

    sunburst_labels = [
        "AI Strategic Foundations",
        # L1
        "AI Strategy", "AI Agents", "GenAI Delivery",
        "Governance", "ISO 42001", "Client Experience", "Adoption",
        # L2 — Strategy
        "Value Creation", "Strategy Canvas", "Archetypes",
        # L2 — Agents
        "ReAct Pattern", "Multi-Agent", "Tool Use", "Memory-Aug.",
        # L2 — GenAI
        "Support Bots", "Back-Office", "Knowledge Mgmt",
        # L2 — Governance
        "Fairness", "Transparency", "Accountability", "Safety",
        # L2 — ISO
        "Context", "Leadership", "Planning", "Operation", "Improvement",
        # L2 — CX
        "Personalisation", "Proactive Svc", "Quality AI",
        # L2 — Adoption
        "Clarity", "Capability", "Culture", "Collaboration", "Continuity",
    ]
    sunburst_parents = [
        "",
        # L1
        "AI Strategic Foundations", "AI Strategic Foundations", "AI Strategic Foundations",
        "AI Strategic Foundations", "AI Strategic Foundations", "AI Strategic Foundations",
        "AI Strategic Foundations",
        # L2 — Strategy
        "AI Strategy", "AI Strategy", "AI Strategy",
        # L2 — Agents
        "AI Agents", "AI Agents", "AI Agents", "AI Agents",
        # L2 — GenAI
        "GenAI Delivery", "GenAI Delivery", "GenAI Delivery",
        # L2 — Governance
        "Governance", "Governance", "Governance", "Governance",
        # L2 — ISO
        "ISO 42001", "ISO 42001", "ISO 42001", "ISO 42001", "ISO 42001",
        # L2 — CX
        "Client Experience", "Client Experience", "Client Experience",
        # L2 — Adoption
        "Adoption", "Adoption", "Adoption", "Adoption", "Adoption",
    ]
    sunburst_vals = [1] * len(sunburst_labels)
    sunburst_vals[0] = 0

    fig_sun = go.Figure(go.Sunburst(
        labels=sunburst_labels,
        parents=sunburst_parents,
        values=sunburst_vals,
        branchvalues="total",
        textfont=dict(size=11),
        insidetextorientation="radial",
        marker=dict(colorscale="Blues"),
    ))
    fig_sun.update_layout(height=480, margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(fig_sun, use_container_width=True)

    st.markdown("---")

    # ── Chart 2: 5-C Framework radar  +  AI Adoption Roadmap ────────────
    st.markdown("### Key Frameworks")
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("#### 5-C AI Adoption Framework")
        five_c = ["Clarity", "Capability", "Culture", "Collaboration", "Continuity"]
        five_c_desc = [
            "Define & communicate the AI vision",
            "Build skills & champion networks",
            "Psychological safety to experiment",
            "Break silos — biz, tech, data, risk",
            "Embed AI into BAU & OKRs",
        ]
        five_c_scores = [90, 85, 75, 80, 70]

        fig_5c = go.Figure()
        fig_5c.add_trace(go.Scatterpolar(
            r=five_c_scores + [five_c_scores[0]],
            theta=five_c + [five_c[0]],
            fill="toself",
            fillcolor="rgba(25,118,210,0.2)",
            line=dict(color="#1976d2", width=2.5),
            mode="lines+markers+text",
            text=[""] * 5 + [""],
            name="Importance",
        ))
        fig_5c.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100],
                                       tickvals=[25, 50, 75, 100])),
            showlegend=False,
            height=340,
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_5c, use_container_width=True)
        for c, d in zip(five_c, five_c_desc):
            st.markdown(f"**{c}** — {d}")

    with col_b:
        st.markdown("#### AI Adoption Roadmap")
        phases = ["Explore", "Pilot", "Scale", "Optimise"]
        starts = [0, 3, 6, 12]
        ends   = [3, 6, 12, 18]
        focus  = [
            "Use-case ID · Awareness · Exec buy-in",
            "2–3 pilots · Feedback loops · Champions",
            "Productionise · Centre of Excellence · Governance",
            "Continuous improvement · Next use-cases",
        ]
        colors = ["#bbdefb", "#64b5f6", "#1976d2", "#0d47a1"]

        fig_road = go.Figure()
        for i, (ph, s, e, f, c) in enumerate(zip(phases, starts, ends, focus, colors)):
            fig_road.add_trace(go.Bar(
                x=[e - s], y=[ph], orientation="h",
                base=s,
                marker_color=c,
                text=f"<b>{ph}</b><br>{f}",
                textposition="inside",
                insidetextanchor="middle",
                name=ph,
                hovertemplate=f"<b>{ph}</b><br>Month {s}–{e}<br>{f}<extra></extra>",
            ))
        fig_road.update_layout(
            barmode="stack",
            xaxis=dict(title="Month", tickvals=list(range(0, 19, 3)),
                       ticktext=[f"M{m}" for m in range(0, 19, 3)]),
            yaxis=dict(title=""),
            showlegend=False,
            height=340,
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_road, use_container_width=True)

        roadmap_df = pd.DataFrame({
            "Phase": phases,
            "Timeline": [f"Month {s}–{e}" for s, e in zip(starts, ends)],
            "Focus": focus,
        })
        st.dataframe(roadmap_df, use_container_width=True, hide_index=True)

    st.markdown("---")

    # ── Chart 3: AI Risk Heatmap  +  ISO 42001 Gauge ────────────────────
    st.markdown("### Governance Snapshot")
    col_c, col_d = st.columns(2)

    with col_c:
        st.markdown("#### AI Risk Heatmap")

        # Each risk: (name, likelihood, impact, dot_x, dot_y, label_x, label_y, color)
        # Dot positions are jittered where risks share a zone; label positions avoid overlap
        risks = [
            ("Model Bias",    3, 3,  2.80, 3.15,  1.90, 3.70, "red"),
            ("Hallucination", 3, 3,  3.20, 2.85,  3.90, 2.40, "red"),
            ("Data Breach",   2, 4,  1.85, 3.90,  0.90, 4.30, "red"),
            ("Regulatory",    2, 4,  2.15, 4.10,  2.20, 4.45, "red"),
            ("Model Drift",   3, 2,  2.80, 1.85,  1.90, 1.45, "orange"),
            ("Shadow AI",     3, 2,  3.20, 2.15,  4.00, 1.70, "orange"),
            ("Over-reliance", 2, 2,  2.00, 2.00,  1.00, 1.60, "gold"),
        ]

        fig_risk = go.Figure()
        # Background zones
        for x0, y0, x1, y1, col in [
            (0.5, 0.5, 2.5, 2.5, "rgba(76,175,80,0.12)"),
            (2.5, 2.5, 4.5, 4.5, "rgba(244,67,54,0.12)"),
            (0.5, 2.5, 2.5, 4.5, "rgba(255,152,0,0.12)"),
            (2.5, 0.5, 4.5, 2.5, "rgba(255,152,0,0.12)"),
        ]:
            fig_risk.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1,
                               fillcolor=col, line_width=0)

        # Plot each dot individually and add an annotation arrow to the label
        for name, _lh, _imp, dx, dy, lx, ly, c in risks:
            fig_risk.add_trace(go.Scatter(
                x=[dx], y=[dy], mode="markers",
                marker=dict(size=16, color=c, line=dict(color="white", width=2)),
                hovertemplate=f"<b>{name}</b><br>Likelihood: {_lh}/4<br>Impact: {_imp}/4<extra></extra>",
                showlegend=False,
            ))
            fig_risk.add_annotation(
                x=dx, y=dy, ax=lx, ay=ly,
                text=f"<b>{name}</b>",
                showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.2,
                arrowcolor="#555", font=dict(size=11),
                xref="x", yref="y", axref="x", ayref="y",
                bgcolor="rgba(255,255,255,0.85)", borderpad=3,
            )

        fig_risk.add_annotation(x=1.5, y=1.0, text="LOW RISK", showarrow=False,
                                font=dict(color="green", size=10, family="Arial Black"), opacity=0.5)
        fig_risk.add_annotation(x=3.5, y=4.0, text="HIGH RISK", showarrow=False,
                                font=dict(color="red", size=10, family="Arial Black"), opacity=0.5)
        fig_risk.add_annotation(x=1.5, y=4.0, text="MEDIUM", showarrow=False,
                                font=dict(color="darkorange", size=9), opacity=0.5)
        fig_risk.add_annotation(x=3.5, y=1.0, text="MEDIUM", showarrow=False,
                                font=dict(color="darkorange", size=9), opacity=0.5)

        fig_risk.update_layout(
            xaxis=dict(title="Likelihood", range=[0.5, 4.5],
                       tickvals=[1, 2, 3, 4],
                       ticktext=["Low", "Med-Low", "Medium", "High"]),
            yaxis=dict(title="Impact", range=[0.5, 4.5],
                       tickvals=[1, 2, 3, 4],
                       ticktext=["Low", "Med-Low", "Medium", "Very High"]),
            height=420,
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_risk, use_container_width=True)

    with col_d:
        st.markdown("#### ISO 42001 Clause Coverage")
        iso_clauses = ["Context", "Leadership", "Planning", "Support",
                       "Operation", "Perf. Eval.", "Improvement"]
        iso_coverage = [70, 65, 60, 55, 50, 45, 40]

        fig_iso = go.Figure()
        fig_iso.add_trace(go.Bar(
            x=iso_coverage, y=iso_clauses,
            orientation="h",
            marker=dict(
                color=iso_coverage,
                colorscale=[[0, "#bbdefb"], [0.5, "#1976d2"], [1, "#0d47a1"]],
                showscale=False,
            ),
            text=[f"{v}%" for v in iso_coverage],
            textposition="outside",
        ))
        fig_iso.add_vline(x=80, line_dash="dash", line_color="red",
                          annotation_text="Target 80%", annotation_position="top right")
        fig_iso.update_layout(
            xaxis=dict(title="Compliance Coverage %", range=[0, 105]),
            yaxis=dict(title=""),
            height=360,
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_iso, use_container_width=True)

    st.markdown("---")

    # ── Chart 4: Maturity Radar (interactive) ───────────────────────────
    st.markdown("### AI Maturity Self-Assessment")
    st.caption("Rate your organisation's current maturity across the seven dimensions (1 = Early · 5 = Leading)")

    dims = [
        "AI Strategy", "Agentic AI", "GenAI Delivery",
        "Governance", "ISO 42001", "Client Experience", "Adoption"
    ]
    scores = []
    cols = st.columns(7)
    for i, (col, dim) in enumerate(zip(cols, dims)):
        with col:
            scores.append(st.slider(dim, 1, 5, 3, key=f"radar_{i}"))

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[5] * len(dims) + [5],
        theta=dims + [dims[0]],
        fill="toself",
        fillcolor="rgba(244,67,54,0.07)",
        line=dict(color="rgba(244,67,54,0.3)", dash="dot"),
        name="Leading (5)",
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],
        theta=dims + [dims[0]],
        fill="toself",
        fillcolor="rgba(79,195,247,0.25)",
        line=dict(color="#4fc3f7", width=2.5),
        name="Your Org",
        mode="lines+markers",
        marker=dict(size=7),
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        legend=dict(orientation="h"),
        height=420,
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    avg = sum(scores) / len(scores)
    level = "Leading" if avg >= 4.5 else "Advanced" if avg >= 3.5 else "Developing" if avg >= 2.5 else "Emerging"
    st.info(f"Average maturity score: **{avg:.1f} / 5** — **{level}** stage")


# ──────────────────────────────────────────────
# MODULE 1 — AI STRATEGIC FOUNDATIONS
# ──────────────────────────────────────────────

elif selected == "🎯 AI Strategic Foundations":
    st.title("🎯 AI Strategic Foundations")
    st.markdown("*How to think about AI as a strategic asset and build an enterprise AI vision.*")

    tab1, tab2, tab3 = st.tabs(["Core Concepts", "Value Framework", "Strategy Canvas"])

    with tab1:
        st.markdown("#### What is AI Strategy?")
        st.markdown("""
        AI Strategy is the deliberate alignment of artificial intelligence investments with
        business objectives to generate sustainable competitive advantage.
        """)

        st.markdown("**Key Pillars**")
        for pill in ["Value Creation", "Data Assets", "Talent & Culture",
                     "Technology Stack", "Ethics & Trust", "Operating Model"]:
            st.markdown(f'<span class="concept-pill">{pill}</span>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### Strategic AI Archetypes")
        archetypes = pd.DataFrame({
            "Archetype": ["Efficiency Leader", "Product Innovator", "Data Monetiser", "Experience Champion"],
            "Primary Goal": ["Cost reduction via automation", "AI-native products & services",
                             "Sell data/insights as products", "Hyper-personalised customer journeys"],
            "AI Priority": ["RPA + Predictive", "GenAI + Agents", "ML + Analytics", "Recommendation + NLP"],
            "Key Risk": ["Workforce displacement", "Rapid obsolescence", "Privacy & regulation", "Trust & bias"],
        })
        st.dataframe(archetypes, use_container_width=True, hide_index=True)

    with tab2:
        st.markdown("#### AI Value Framework")
        categories = ["Revenue Growth", "Cost Reduction", "Risk Mitigation",
                      "Speed to Market", "Customer Satisfaction", "Employee Experience"]
        values = [85, 92, 70, 78, 88, 65]
        fig = px.bar(
            x=values, y=categories, orientation="h",
            color=values, color_continuous_scale="Blues",
            labels={"x": "Impact Score (0–100)", "y": ""},
            title="Average AI Impact by Value Category (Industry Benchmark)"
        )
        fig.update_layout(coloraxis_showscale=False, height=350)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="highlight-box">
        <strong>Key Insight:</strong> Organisations with a formal AI strategy achieve 2.5× greater
        value realisation compared to those pursuing ad-hoc AI initiatives.
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("#### AI Strategy Canvas Builder")
        col1, col2 = st.columns(2)
        with col1:
            st.text_area("Business Objectives", placeholder="e.g. Grow revenue 20%, reduce ops cost by 15%...", height=100)
            st.text_area("Key AI Capabilities Needed", placeholder="e.g. Predictive analytics, NLP, Computer Vision...", height=100)
            st.text_area("Data Assets Available", placeholder="e.g. CRM data, transaction logs, support tickets...", height=100)
        with col2:
            st.text_area("Quick Wins (0–6 months)", placeholder="e.g. AI-powered FAQ bot, churn prediction...", height=100)
            st.text_area("Strategic Bets (6–18 months)", placeholder="e.g. Autonomous service agents...", height=100)
            st.text_area("Known Risks & Constraints", placeholder="e.g. Data quality, regulation, talent gaps...", height=100)
        if st.button("💾 Save Canvas"):
            st.success("Canvas saved to session. Use this as input for your AI roadmap.")


# ──────────────────────────────────────────────
# MODULE 2 — AI AGENTS & AUTONOMOUS SYSTEMS
# ──────────────────────────────────────────────

elif selected == "🤖 AI Agents & Autonomous Systems":
    st.title("🤖 AI Agents & Autonomous Systems")
    st.markdown("*From reactive bots to autonomous agents that plan, act, and learn.*")

    tab1, tab2, tab3 = st.tabs(["Agent Architecture", "Agent Types", "Design Patterns"])

    with tab1:
        st.markdown("#### What is an AI Agent?")
        st.markdown("""
        An AI agent is a software system that **perceives** its environment, **reasons** about goals,
        **plans** actions, **executes** them through tools, and **learns** from outcomes — with
        minimal or no human intervention per cycle.
        """)

        st.markdown("#### Core Components")
        components = {
            "Perception": "Reads inputs — text, data, APIs, sensors",
            "Memory": "Short-term context + long-term knowledge stores",
            "Reasoning / LLM Core": "Plans next step; selects tools; reflects on results",
            "Tool Use": "Calls APIs, writes code, queries databases, browses web",
            "Action": "Executes tasks — emails, code commits, form fills",
            "Feedback Loop": "Evaluates outcome; adjusts strategy if needed",
        }
        for comp, desc in components.items():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{comp}**")
            with col2:
                st.markdown(desc)

    with tab2:
        st.markdown("#### Agent Taxonomy")
        agent_types = pd.DataFrame({
            "Agent Type": ["Reactive", "Deliberative", "Hybrid", "Multi-Agent", "Autonomous"],
            "Decision Style": ["Rule-based / reflex", "Plans ahead", "Reflex + planning",
                               "Collaborative swarm", "Self-directed over long horizon"],
            "Example": ["Chatbot FAQ", "Route optimiser", "Customer service agent",
                        "AI research team", "Autonomous software engineer"],
            "Autonomy Level": ["Low", "Medium", "Medium-High", "High", "Very High"],
        })
        st.dataframe(agent_types, use_container_width=True, hide_index=True)

        st.markdown("#### Autonomy Spectrum")
        autonomy_labels = ["Human-in-loop", "Human-on-loop", "Human-out-of-loop"]
        autonomy_vals = [30, 65, 95]
        fig = go.Figure(go.Bar(
            x=autonomy_labels, y=autonomy_vals,
            marker_color=["#42a5f5", "#1976d2", "#0d47a1"],
            text=[f"{v}% autonomy" for v in autonomy_vals],
            textposition="auto"
        ))
        fig.update_layout(yaxis_title="Autonomy %", height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("#### Common Agentic Design Patterns")
        patterns = [
            ("ReAct", "Reason → Act → Observe loop. Agent thinks aloud before each action."),
            ("Plan & Execute", "Upfront planning phase followed by sequential execution with re-planning on failure."),
            ("Reflection", "Agent critiques its own output and iterates to improve quality."),
            ("Tool Use", "Agent selects from a registry of tools (functions/APIs) to accomplish subtasks."),
            ("Multi-Agent Orchestration", "Orchestrator decomposes tasks; specialist sub-agents execute in parallel."),
            ("Memory-Augmented", "Agent queries a vector store for long-term episodic or semantic memory."),
        ]
        for name, desc in patterns:
            with st.expander(f"**{name}**"):
                st.write(desc)


# ──────────────────────────────────────────────
# MODULE 3 — GENERATIVE AI FOR SERVICE DELIVERY
# ──────────────────────────────────────────────

elif selected == "✨ Generative AI for Service Delivery":
    st.title("✨ Generative AI for Service Delivery")
    st.markdown("*Transforming how services are designed, delivered, and measured.*")

    tab1, tab2, tab3 = st.tabs(["Use Cases", "ROI Estimator", "Prompt Engineering"])

    with tab1:
        st.markdown("#### High-Impact GenAI Use Cases in Service Delivery")

        use_cases = {
            "Customer Support": [
                "AI-powered first-line resolution (chatbots / voice)",
                "Agent assist — real-time knowledge surfacing",
                "Automatic ticket summarisation & categorisation",
                "Sentiment-based escalation routing",
            ],
            "Back-Office Operations": [
                "Document intelligence & data extraction",
                "Contract review and clause flagging",
                "Automated report generation",
                "Code generation for internal tools",
            ],
            "Knowledge Management": [
                "Enterprise search with natural language queries",
                "Auto-updating FAQ & knowledge bases",
                "Onboarding content generation",
                "Meeting summarisation & action extraction",
            ],
        }
        for category, items in use_cases.items():
            with st.expander(f"**{category}**", expanded=True):
                for item in items:
                    st.markdown(f"- {item}")

    with tab2:
        st.markdown("#### GenAI ROI Quick Estimator")
        col1, col2 = st.columns(2)
        with col1:
            agents_n = st.number_input("Number of service agents", 10, 10000, 200)
            avg_salary = st.number_input("Average annual salary (£)", 20000, 150000, 35000, step=1000)
            time_saved_pct = st.slider("Estimated time saving per agent (%)", 5, 50, 20)
        with col2:
            impl_cost = st.number_input("Implementation cost (£)", 10000, 5000000, 150000, step=10000)
            run_cost = st.number_input("Annual run cost (£)", 5000, 1000000, 50000, step=5000)

        annual_saving = agents_n * avg_salary * (time_saved_pct / 100)
        net_year1 = annual_saving - impl_cost - run_cost
        net_year3 = (annual_saving * 3) - impl_cost - (run_cost * 3)
        roi_year1 = (net_year1 / (impl_cost + run_cost)) * 100 if (impl_cost + run_cost) else 0

        r1, r2, r3 = st.columns(3)
        r1.metric("Annual Labour Saving", f"£{annual_saving:,.0f}")
        r2.metric("Net Year 1 Benefit", f"£{net_year1:,.0f}")
        r3.metric("ROI Year 1", f"{roi_year1:.1f}%")
        st.metric("Net 3-Year Benefit", f"£{net_year3:,.0f}")

    with tab3:
        st.markdown("#### Prompt Engineering Essentials")
        techniques = pd.DataFrame({
            "Technique": ["Zero-shot", "Few-shot", "Chain-of-Thought", "System Prompt", "RAG", "Tool Use"],
            "When to Use": [
                "Simple, well-defined tasks",
                "Tasks needing consistent format/style",
                "Complex reasoning or multi-step problems",
                "Setting persona, constraints, output format",
                "Need up-to-date or proprietary knowledge",
                "Need to call APIs or perform actions",
            ],
            "Example": [
                "Classify this ticket as Billing/Tech/Other",
                "Given examples: ... Now classify: ...",
                "Think step by step: ...",
                "You are a senior support analyst. Always respond in JSON.",
                "Search knowledge base then answer",
                "Use search_tool() to find the order status",
            ],
        })
        st.dataframe(techniques, use_container_width=True, hide_index=True)


# ──────────────────────────────────────────────
# MODULE 4 — AI GOVERNANCE, ETHICS & RISK
# ──────────────────────────────────────────────

elif selected == "⚖️ AI Governance, Ethics & Risk":
    st.title("⚖️ AI Governance, Ethics & Risk")
    st.markdown("*Building trustworthy AI through principled design and accountable governance.*")

    tab1, tab2, tab3 = st.tabs(["Principles", "Risk Register", "Governance Model"])

    with tab1:
        st.markdown("#### Responsible AI Principles")
        principles = [
            ("Fairness", "AI systems must not discriminate unfairly across protected characteristics.",
             "Bias audits, fairness metrics, diverse training data"),
            ("Transparency", "Stakeholders should understand how AI decisions are made.",
             "Explainability tools, model cards, audit logs"),
            ("Accountability", "Clear ownership of AI outcomes, with human oversight.",
             "RACI for AI, escalation paths, appeals processes"),
            ("Privacy", "Personal data used only as authorised, with minimal retention.",
             "Data minimisation, differential privacy, GDPR compliance"),
            ("Safety & Security", "AI must not cause harm or be exploitable.",
             "Red-teaming, adversarial testing, input validation"),
            ("Reliability", "AI outputs should be consistent, accurate, and well-calibrated.",
             "Monitoring, drift detection, human-in-the-loop gates"),
        ]
        for name, desc, controls in principles:
            with st.expander(f"**{name}**"):
                st.markdown(f"**Principle:** {desc}")
                st.markdown(f"**Controls:** {controls}")

    with tab2:
        st.markdown("#### AI Risk Register")
        risks = pd.DataFrame({
            "Risk": ["Model Bias", "Hallucination", "Data Breach", "Regulatory Non-compliance",
                     "Model Drift", "Shadow AI", "Over-reliance"],
            "Likelihood": ["High", "High", "Medium", "Medium", "High", "High", "Medium"],
            "Impact": ["High", "High", "Very High", "Very High", "Medium", "Medium", "Medium"],
            "Mitigation": [
                "Fairness testing, diverse data",
                "RAG grounding, output validation",
                "Encryption, access controls, DLP",
                "EU AI Act mapping, legal review",
                "Continuous monitoring, retraining pipeline",
                "AI governance policy, approved tool list",
                "Training, human-in-loop checkpoints",
            ],
            "Owner": ["Data Science", "AI Engineering", "InfoSec", "Legal/Compliance",
                      "MLOps", "CIO Office", "Change Management"],
        })
        st.dataframe(risks, use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("#### Three Lines of AI Governance")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**1st Line — Business**")
            st.markdown("""
            - AI Product Owners
            - Delivery Teams
            - Day-to-day controls
            - Risk acceptance
            """)
        with col2:
            st.markdown("**2nd Line — Risk & Compliance**")
            st.markdown("""
            - AI Ethics Board
            - Risk function
            - Policy & standards
            - Regulatory monitoring
            """)
        with col3:
            st.markdown("**3rd Line — Audit**")
            st.markdown("""
            - Internal Audit
            - Independent assurance
            - AI system audits
            - Regulatory reviews
            """)

        st.markdown("---")
        st.markdown("""
        <div class="highlight-box">
        <strong>EU AI Act Reminder:</strong> High-risk AI systems (hiring, credit, biometrics,
        critical infrastructure) require mandatory conformity assessments, human oversight,
        and registration in the EU AI database before deployment.
        </div>
        """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# MODULE 5 — ISO 42001
# ──────────────────────────────────────────────

elif selected == "📋 ISO 42001":
    st.title("📋 ISO 42001 — AI Management Systems")
    st.markdown("*The international standard for establishing, implementing, and continually improving an AI Management System (AIMS).*")

    tab1, tab2, tab3 = st.tabs(["Standard Overview", "Clause Map", "Gap Assessment"])

    with tab1:
        st.markdown("#### What is ISO 42001?")
        st.markdown("""
        ISO/IEC 42001:2023 is the world's first international standard for **AI Management Systems (AIMS)**.
        It provides a structured framework for organisations to manage AI responsibly across the full lifecycle —
        from strategy and design through to deployment, monitoring, and improvement.
        """)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Who should certify?**")
            for item in ["AI product developers", "AI service providers",
                         "Organisations deploying AI in high-risk contexts",
                         "Any organisation seeking third-party assurance"]:
                st.markdown(f"- {item}")
        with col2:
            st.markdown("**Key Benefits**")
            for item in ["Builds stakeholder trust", "Reduces AI-related risk",
                         "Supports regulatory readiness (EU AI Act)",
                         "Competitive differentiator", "Drives continuous improvement"]:
                st.markdown(f"- {item}")

    with tab2:
        st.markdown("#### ISO 42001 Clause Structure")
        clauses = pd.DataFrame({
            "Clause": [
                "4 — Context", "5 — Leadership", "6 — Planning",
                "7 — Support", "8 — Operation", "9 — Performance Evaluation", "10 — Improvement"
            ],
            "Key Requirements": [
                "Understand org context, stakeholders, scope of AIMS",
                "Top management commitment, AI policy, roles & responsibilities",
                "AI risk & opportunity assessment, objectives & planning",
                "Resources, competence, awareness, communication, documented info",
                "Operational planning, AI risk treatment, AI system lifecycle controls",
                "Monitoring, measurement, internal audit, management review",
                "Nonconformity, corrective action, continual improvement",
            ],
            "PDCA Phase": ["Plan", "Plan", "Plan", "Support", "Do", "Check", "Act"],
        })
        st.dataframe(clauses, use_container_width=True, hide_index=True)

        st.markdown("**Annex A — Controls**")
        st.markdown("""
        ISO 42001 Annex A provides **38 controls** across 9 domains covering:
        policies, processes, impact assessment, data governance, transparency,
        human oversight, and third-party management.
        """)

    with tab3:
        st.markdown("#### ISO 42001 Gap Assessment")
        st.caption("Score each clause area from 0 (not started) to 4 (fully implemented)")

        clause_labels = ["Context", "Leadership", "Planning", "Support",
                         "Operation", "Performance Eval.", "Improvement"]
        clause_scores = []
        cols = st.columns(7)
        for col, label in zip(cols, clause_labels):
            with col:
                clause_scores.append(st.select_slider(
                    label, options=[0, 1, 2, 3, 4], value=2, key=f"iso_{label}"
                ))

        target = [4] * 7
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=target + [target[0]], theta=clause_labels + [clause_labels[0]],
            fill="toself", fillcolor="rgba(25,118,210,0.1)",
            line=dict(color="#1976d2", dash="dash"), name="Target (4)"
        ))
        fig.add_trace(go.Scatterpolar(
            r=clause_scores + [clause_scores[0]], theta=clause_labels + [clause_labels[0]],
            fill="toself", fillcolor="rgba(79,195,247,0.3)",
            line=dict(color="#4fc3f7", width=2), name="Current State"
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 4])),
            height=400, legend=dict(orientation="h"),
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

        gap_total = sum(target) - sum(clause_scores)
        st.metric("Total Gap Score", f"{gap_total} / 28 points", delta=f"-{gap_total} from full compliance")


# ──────────────────────────────────────────────
# MODULE 6 — AI-DRIVEN CLIENT EXPERIENCE
# ──────────────────────────────────────────────

elif selected == "💼 AI-driven Client Experience & Service Quality":
    st.title("💼 AI-driven Client Experience & Service Quality")
    st.markdown("*Using AI to delight clients, predict needs, and continuously raise service standards.*")

    tab1, tab2, tab3 = st.tabs(["CX Capabilities", "Quality Metrics", "Journey Mapping"])

    with tab1:
        st.markdown("#### AI Capabilities Transforming Client Experience")
        capabilities = {
            "Personalisation at Scale": [
                "Next-best-action recommendations",
                "Dynamic content and offer tailoring",
                "Personalised communication cadence & channel",
            ],
            "Proactive Service": [
                "Predictive churn models with retention triggers",
                "Anomaly detection for service disruption alerts",
                "Proactive issue resolution before client notices",
            ],
            "Intelligent Interaction": [
                "Conversational AI for 24/7 self-service",
                "Emotion & sentiment analysis on all interactions",
                "Real-time agent assist for complex queries",
            ],
            "Quality Assurance": [
                "Automated call / chat transcript scoring",
                "AI-powered CSAT & NPS prediction",
                "Root-cause analysis of negative experiences",
            ],
        }
        for category, items in capabilities.items():
            with st.expander(f"**{category}**", expanded=True):
                for item in items:
                    st.markdown(f"- {item}")

    with tab2:
        st.markdown("#### AI-Enhanced Service Quality KPIs")
        kpi_data = pd.DataFrame({
            "KPI": ["First Contact Resolution", "Average Handle Time", "CSAT Score",
                    "NPS", "Churn Rate", "SLA Adherence"],
            "Baseline (Pre-AI)": [68, 420, 72, 32, 8.5, 89],
            "With AI (Target)": [84, 290, 86, 51, 4.2, 97],
            "Unit": ["%", "seconds", "/100", "score", "%", "%"],
        })
        kpi_data["Improvement"] = kpi_data.apply(
            lambda r: f"+{r['With AI (Target)'] - r['Baseline (Pre-AI)']:.1f} {r['Unit']}"
            if r["KPI"] not in ["Average Handle Time", "Churn Rate"]
            else f"-{r['Baseline (Pre-AI)'] - r['With AI (Target)']:.1f} {r['Unit']}",
            axis=1
        )
        st.dataframe(kpi_data[["KPI", "Baseline (Pre-AI)", "With AI (Target)", "Improvement"]],
                     use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("#### AI Touchpoints Across the Client Journey")
        journey_stages = ["Awareness", "Onboarding", "Usage", "Support", "Renewal", "Advocacy"]
        ai_apps = [
            "Predictive targeting, personalised ads",
            "AI document check, smart welcome flow",
            "Usage analytics, proactive tips",
            "Conversational AI, agent assist, sentiment analysis",
            "Churn prediction, personalised retention offer",
            "NPS analysis, referral propensity model",
        ]
        impact = [65, 80, 70, 92, 85, 60]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=journey_stages, y=impact,
            marker_color="#1976d2",
            text=[f"{v}% impact" for v in impact],
            textposition="auto",
        ))
        fig.update_layout(
            yaxis_title="AI Impact Score", height=300,
            title="AI Impact by Journey Stage"
        )
        st.plotly_chart(fig, use_container_width=True)

        for stage, app in zip(journey_stages, ai_apps):
            st.markdown(f"**{stage}:** {app}")


# ──────────────────────────────────────────────
# MODULE 7 — LEADING AI ADOPTION
# ──────────────────────────────────────────────

elif selected == "🚀 Leading AI Adoption in Delivery Teams":
    st.title("🚀 Leading AI Adoption in Delivery Teams")
    st.markdown("*Turning AI ambition into practice: change leadership, upskilling, and sustaining momentum.*")

    tab1, tab2, tab3 = st.tabs(["Change Framework", "Adoption Roadmap", "Readiness Check"])

    with tab1:
        st.markdown("#### The 5-C AI Adoption Framework")
        cs = [
            ("Clarity", "Define the AI vision, articulate the 'why', and communicate consistently across the organisation."),
            ("Capability", "Build skills through targeted training, communities of practice, and AI champion networks."),
            ("Culture", "Foster psychological safety to experiment, fail fast, and share learnings openly."),
            ("Collaboration", "Break silos — AI succeeds when business, tech, data, and risk work as one team."),
            ("Continuity", "Embed AI into BAU processes, OKRs, and performance conversations to sustain change."),
        ]
        for name, desc in cs:
            col1, col2 = st.columns([1, 5])
            with col1:
                st.markdown(f"<div style='font-size:2em; text-align:center'>{'🎯📚🌱🤝🔄'[list(dict(cs).keys()).index(name) if False else ['Clarity','Capability','Culture','Collaboration','Continuity'].index(name)]}</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"**{name}:** {desc}")
            st.markdown("")

    with tab2:
        st.markdown("#### AI Adoption Roadmap")
        roadmap = pd.DataFrame({
            "Phase": ["Explore (0–3m)", "Pilot (3–6m)", "Scale (6–12m)", "Optimise (12–18m)"],
            "Focus": [
                "Use-case identification, team awareness",
                "2–3 high-value pilots with tight feedback loops",
                "Productionise pilots, widen to more teams",
                "Continuous improvement, new use-cases",
            ],
            "Key Activities": [
                "AI literacy workshops, opportunity mapping, exec sponsorship",
                "Agile sprints, champion training, quick-win demos",
                "Centre of Excellence, governance uplift, tooling standardisation",
                "Value tracking, lessons learned, next-cycle planning",
            ],
            "Success Metric": [
                "# of opportunities identified, awareness score",
                "Pilot ROI, user adoption %, feedback NPS",
                "# teams using AI, cost / quality KPIs",
                "Sustained ROI, time-to-value for new use-cases",
            ],
        })
        st.dataframe(roadmap, use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("#### Team AI Readiness Check")
        questions = [
            ("Leadership Alignment", "Senior leaders actively sponsor and participate in AI initiatives"),
            ("Data Availability", "We have access to clean, relevant data for our target use cases"),
            ("Technical Skills", "The team has (or can access) skills in ML, data engineering, and AI tooling"),
            ("Process Clarity", "We have well-documented processes that AI can augment or automate"),
            ("Change Appetite", "Team members are open to changing how they work with AI assistance"),
            ("Governance Readiness", "We have (or are building) AI governance policies and oversight"),
        ]
        total = 0
        for i, (title, stmt) in enumerate(questions):
            val = st.slider(f"**{title}**\n_{stmt}_", 1, 5, 3, key=f"ready_{i}")
            total += val

        max_score = len(questions) * 5
        pct = int((total / max_score) * 100)
        st.markdown("---")
        st.markdown(f"**Overall Readiness Score: {total}/{max_score} ({pct}%)**")
        st.progress(pct / 100)

        if pct >= 75:
            st.success("High readiness — proceed with scaled AI adoption. Focus on governance and speed.")
        elif pct >= 50:
            st.warning("Moderate readiness — address gaps in weakest dimensions before scaling.")
        else:
            st.error("Low readiness — invest in foundations (data, skills, leadership) before piloting.")
