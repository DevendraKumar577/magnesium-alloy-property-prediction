
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="Mg Alloy ML Predictor",
    page_icon="🧪",
    layout="wide"
)



# Custom UI Styling
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #F4F7FB;
}

/* Main Container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Main Headings */
h1 {
    color: #142D4E !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #193B63 !important;
    font-weight: 700 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #EAF0F8;
    border-right: 1px solid #D9E2EF;
}

/* Metric Cards */
div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E0E7F0;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(20,45,78,0.05);
}

/* Buttons */
.stButton > button {
    background: #1769AA;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.5rem;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #104E83;
    color: white;
    border: none;
}

/* Slider */
.stSlider [data-baseweb="slider"] {
    margin-top: 10px;
}

/* Divider */
hr {
    border-color: #DCE5EF;
}

/* Success Message */
div[data-testid="stAlert"] {
    border-radius: 10px;
}


/* Premium Hero Header */
.hero-section {
    background: linear-gradient(120deg, #102B4E, #1769AA);
    padding: 35px 38px;
    border-radius: 18px;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(16,43,78,0.15);
}

.hero-section h1 {
    color: white !important;
    font-size: 36px !important;
    margin-bottom: 12px;
}

.hero-section p {
    color: #DCEBFA !important;
    font-size: 16px;
    margin-bottom: 0;
}

.hero-tag {
    color: #A9D5FF;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 12px;
}


</style>
""", unsafe_allow_html=True)


# Load trained models
@st.cache_resource
def load_models():
    return joblib.load("best_models.pkl")


best_models = load_models()


# Property prediction function
def predict_properties(y_value):

    X_input = pd.DataFrame({
        "Y_wt_pct": [y_value]
    })

    predictions = {}

    for target, model in best_models.items():

        prediction = model.predict(X_input)[0]

        if "Creep_Rate" in target:
            prediction = np.power(10, prediction)

        predictions[target] = float(prediction)

    return predictions


# Calculate dynamic performance score
def calculate_performance():

    y_values = np.linspace(0, 8, 81)

    property_data = []

    for y in y_values:

        predictions = predict_properties(y)

        property_data.append({
            "Y_wt_pct": y,
            **predictions
        })

    df = pd.DataFrame(property_data)

    score_columns = [
        "Tensile_UTS_MPa_SYNTHETIC",
        "Compressive_Strength_MPa_SYNTHETIC",
        "Hardness_HV_SYNTHETIC",
        "Fatigue_Strength_MPa_SYNTHETIC",
        "Creep_Rate_s-1_SYNTHETIC"
    ]

    # Normalize each property between 0 and 100
    normalized = pd.DataFrame()

    for column in score_columns:

        minimum = df[column].min()
        maximum = df[column].max()

        if np.isclose(maximum, minimum):
            normalized[column] = 100.0
            continue

        if column == "Creep_Rate_s-1_SYNTHETIC":
            # Lower creep rate is better
            normalized[column] = (
                (maximum - df[column]) /
                (maximum - minimum) * 100
            )
        else:
            # Higher mechanical strength is better
            normalized[column] = (
                (df[column] - minimum) /
                (maximum - minimum) * 100
            )

    df["Overall_Performance_Score"] = normalized.mean(axis=1)

    best_row = df.loc[
        df["Overall_Performance_Score"].idxmax()
    ]

    return df, best_row, score_columns


# Header

st.markdown("""
<div class="hero-section">
    <div class="hero-tag">MATERIALS SCIENCE • MACHINE LEARNING</div>
    <h1>🧪 Magnesium Alloy Property Prediction</h1>
    <p>
        An intelligent ML-based platform for predicting
        mechanical properties of Mg-Zn-Zr-Y alloys
        using Yttrium concentration.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()



# # Sidebar
# st.sidebar.header("Alloy Composition")

# y_concentration = st.sidebar.slider(
#     "Y Concentration (wt.%)",
#     min_value=0.0,
#     max_value=8.0,
#     value=4.7,
#     step=0.1
# )

# st.sidebar.info(
#     "Enter Y concentration to predict mechanical properties."
# )



# Sidebar
st.sidebar.header("Alloy Composition")

st.sidebar.markdown("### Fixed Elements")

st.sidebar.metric("Zinc (Zn)", "1.00 wt.%")
st.sidebar.metric("Zirconium (Zr)", "0.50 wt.%")

st.sidebar.caption(
    "Zn and Zr concentrations remain fixed."
)

st.sidebar.divider()

st.sidebar.markdown("### Variable Element")

y_concentration = st.sidebar.slider(
    "Yttrium (Y) Concentration (wt.%)",
    min_value=0.0,
    max_value=8.0,
    value=4.7,
    step=0.1
)

# Magnesium as balance element
mg_concentration = 98.5 - y_concentration

st.sidebar.metric(
    "Magnesium (Mg)",
    f"{mg_concentration:.2f} wt.%"
)

st.sidebar.info(
    "Adjust Y concentration to predict mechanical properties. "
    "Mg is calculated as the balance element."
)


# Prediction button
if st.button("Predict Mechanical Properties", type="primary"):

    # Current input predictions
    predictions = predict_properties(y_concentration)

    st.success("Prediction completed successfully!")

    

    
    # Premium Mechanical Properties Section

    st.markdown("""
    <style>
    .property-card {
        background: white;
        padding: 25px 22px;
        border-radius: 16px;
        border: 1px solid #DCE5F0;
        box-shadow: 0 4px 15px rgba(20, 50, 90, 0.06);
         margin-bottom: 18px;
        min-height: 115px;
        transition: 0.2s ease;
    }

    .property-card:hover {
        border-color: #2476B9;
        box-shadow: 0 7px 20px rgba(20, 50, 90, 0.12);
    }

    .property-label {
        color: #64748B;
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 13px;
    }

    .property-value {
        color: #15365B;
        font-size: 29px;
        font-weight: 700;
    }

    .property-unit {
        color: #8290A3;
        font-size: 13px;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("### Predicted Mechanical Properties")
    st.caption(
        f"Predicted results for Yttrium concentration of "
        f"{y_concentration:.2f} wt.%"
    )

    properties = [
        ("Tensile Strength", predictions['Tensile_UTS_MPa_SYNTHETIC'], "MPa"),
        ("Fatigue Strength", predictions['Fatigue_Strength_MPa_SYNTHETIC'], "MPa"),
        ("Compressive Strength", predictions['Compressive_Strength_MPa_SYNTHETIC'], "MPa"),
        ("Creep Rate", predictions['Creep_Rate_s-1_SYNTHETIC'], "s⁻¹"),
        ("Hardness", predictions['Hardness_HV_SYNTHETIC'], "HV")
    ]

    # First row - 3 cards
    row1 = st.columns(3)

    for col, (label, value, unit) in zip(row1, properties[:3]):
        with col:
            if label == "Creep Rate":
                formatted_value = f"{value:.3e}"
            else:
                formatted_value = f"{value:.2f}"

            st.markdown(f"""
            <div class="property-card">
                <div class="property-label">{label}</div>
                <div class="property-value">{formatted_value}</div>
                <div class="property-unit">{unit}</div>
            </div>
            """, unsafe_allow_html=True)

    # Second row - 2 cards
    row2 = st.columns(2)

    for col, (label, value, unit) in zip(row2, properties[3:]):
        with col:
            if label == "Creep Rate":
                formatted_value = f"{value:.3e}"
            else:
                formatted_value = f"{value:.2f}"

            st.markdown(f"""
            <div class="property-card">
                <div class="property-label">{label}</div>
                <div class="property-value">{formatted_value}</div>
                <div class="property-unit">{unit}</div>
            </div>
            """, unsafe_allow_html=True)



    # Dynamic performance analysis
    df, best_row, score_columns = calculate_performance()

    st.divider()

    st.subheader("Overall Performance Analysis")

    
    # Calculate performance metrics
    current_row = df.iloc[
        np.abs(df["Y_wt_pct"] - y_concentration).argmin()
    ]

    current_score = current_row["Overall_Performance_Score"]
    best_score = best_row["Overall_Performance_Score"]
    optimal_y = best_row["Y_wt_pct"]

    score_gap = max(best_score - current_score, 0)
    y_difference = optimal_y - y_concentration

    # Performance Analysis UI
    st.markdown("### 📊 Performance Overview")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.caption("CURRENT PERFORMANCE")
            st.metric(
                "Performance Score",
                f"{current_score:.2f}/100"
            )
            st.progress(
                int(np.clip(current_score, 0, 100))
            )
            st.caption("Score at selected Y concentration")

    with col2:
        with st.container(border=True):
            st.caption("BEST ACHIEVABLE PERFORMANCE")
            st.metric(
                "Best Performance Score",
                 f"{best_score:.2f}/100"
            )
            st.progress(
                int(np.clip(best_score, 0, 100))
            )
            st.caption("Maximum score across the tested range")

        # Optimal composition card
        st.markdown("#### 🎯 Optimal Composition")

        with st.container(border=True):
            col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Optimal Y Concentration",
                f"{optimal_y:.2f} wt.%",
                delta=f"{y_difference:+.2f} wt.% from current"
            )

        with col2:
            st.metric(
                "Performance Improvement Potential",
                f"{score_gap:.2f} points"
            )


    st.divider()

    st.subheader("Performance Score Across Y Concentration")

    
    import plotly.graph_objects as go

    # Prepare graph data
    chart_df = df.sort_values("Y_wt_pct")

    # Find current and optimal composition points
    current_point = df.iloc[
        (df["Y_wt_pct"] - y_concentration).abs().argmin()
    ]

    optimal_point = best_row

    # Create interactive figure
    fig = go.Figure()

    # Main performance curve
    fig.add_trace(go.Scatter(
        x=chart_df["Y_wt_pct"],
        y=chart_df["Overall_Performance_Score"],
        mode="lines",
        name="Performance Curve",
       line=dict(color="#1976D2", width=3),
       hovertemplate=
            "Y Concentration: %{x:.2f} wt.%<br>"
            "Performance Score: %{y:.2f}/100"
            "<extra></extra>"
    ))

    # Current concentration marker
    fig.add_trace(go.Scatter(
        x=[current_point["Y_wt_pct"]],
        y=[current_point["Overall_Performance_Score"]],
        mode="markers",
        name="Current Composition",
        marker=dict(
            color="#F59E0B",
            size=13,
            line=dict(color="white", width=2)
        ),
        hovertemplate=
            "Current Y: %{x:.2f} wt.%<br>"
            "Score: %{y:.2f}/100"
            "<extra></extra>"
    ))

    # Optimal concentration marker
    fig.add_trace(go.Scatter(
        x=[optimal_point["Y_wt_pct"]],
        y=[optimal_point["Overall_Performance_Score"]],
        mode="markers",
        name="Optimal Composition",
        marker=dict(
            color="#16A34A",
            size=15,
            symbol="star",
            line=dict(color="white", width=2)
        ),
        hovertemplate=
            "Optimal Y: %{x:.2f} wt.%<br>"
            "Best Score: %{y:.2f}/100"
            "<extra></extra>"
    ))

    # Chart layout
    fig.update_layout(
        title="Performance Optimization Across Y Concentration",
        xaxis_title="Y Concentration (wt.%)",
        yaxis_title="Overall Performance Score",
        template="plotly_white",
        height=520,
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=20, r=20, t=90, b=40)
    )

    fig.update_xaxes(showgrid=True, gridcolor="#E5E7EB")
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#E5E7EB",
        range=[0, 100]
    )

    st.plotly_chart(fig, use_container_width=True)


    st.caption(
        "Performance scores are calculated using min-max "
        "normalization of the five predicted properties across "
        "the 0–8 wt.% Y concentration range. "
        "Predictions use a synthetic demonstration dataset "
        "and require experimental validation."
    )
