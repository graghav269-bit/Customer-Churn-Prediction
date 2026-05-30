import streamlit as st
import pandas as pd
import os
import sys
import plotly.express as px
import plotly.graph_objects as go

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from models.predict import predict_customer

st.set_page_config(
    page_title="Customer Churn Dashboard",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
[data-testid="stAppViewContainer"]{
    background-color:#F4F7FC;
}

/* Top Header */
[data-testid="stHeader"]{
    background:rgba(0,0,0,0);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #081028 0%,
        #0F1F5C 100%
    );
}

/* Sidebar Text */
[data-testid="stSidebar"] *{
    color:white;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:white;
    border-radius:16px;
    padding:20px;
    box-shadow:
        0px 4px 15px rgba(0,0,0,0.08);
}

/* Main Titles */
h1,h2,h3,h4{
    color:#1A1F36;
}

/* Paragraph Text */
p{
    color:#4A5568;
}

</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "customer_churn_cleaned.csv"
)

df = pd.read_csv(DATA_PATH)

page = st.sidebar.radio(
    "Navigation",
    [
    "Dashboard",
    "Customer Analytics",
    "Churn Insights",
    "Predict Churn",
    "High Risk Customers",
    "Reports"
]
)
st.sidebar.markdown("""
# Churn AI

### Customer Analytics Platform
""")

if page == "Dashboard":

    st.title("📈 Customer Churn Analytics")
    st.caption("Monitor churn risk, customer behavior and revenue impact")

    total_customers = len(df)

    churn_rate = (
        (df["Churn"] == "Yes").mean()
        * 100
    )

    revenue = df["MonthlyCharges"].sum()

    high_risk = int(total_customers * 0.20)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Customers",
        f"{total_customers:,}"
    )

    c2.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

    c3.metric(
        "Revenue",
        f"${revenue:,.0f}"
    )

    c4.metric(
        "High Risk Customers",
        high_risk
    )

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        churn_counts = (
            df["Churn"]
            .value_counts()
            .reset_index()
        )

        churn_counts.columns = [
            "Churn",
            "Count"
        ]

        fig = px.bar(
            churn_counts,
            x="Churn",
            y="Count",
            title="Customer Churn Distribution",
            color="Churn"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        churn_counts = (
            df["Churn"]
            .value_counts()
            .reset_index()
        )

        churn_counts.columns = [
            "Churn",
            "Count"
        ]

        fig2 = px.pie(
            churn_counts,
            names="Churn",
            values="Count",
            hole=0.65,
            title="Customer Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

elif page == "Customer Analytics":

    st.title("📈 Customer Analytics")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            df,
            x="Contract",
            color="Churn",
            title="Contract Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.histogram(
            df,
            x="InternetService",
            color="Churn",
            title="Internet Service Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:

        fig = px.box(
            df,
            x="Churn",
            y="MonthlyCharges",
            title="Monthly Charges Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col4:

        fig = px.box(
            df,
            x="Churn",
            y="tenure",
            title="Tenure Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        
elif page == "Churn Insights":

    st.title("📈 Churn Insights")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Month-to-Month Customers",
            "Highest Churn"
        )

        st.metric(
            "Fiber Optic Users",
            "High Risk"
        )

    with col2:

        st.metric(
            "Low Tenure Customers",
            "Highest Risk"
        )

        st.metric(
            "Electronic Check",
            "High Churn"
        )

    st.markdown("---")

    insights_df = pd.DataFrame({
        "Factor": [
            "Month-to-Month Contract",
            "Fiber Optic Service",
            "Electronic Check",
            "Low Tenure"
        ],
        "Impact Score": [95, 85, 75, 90]
    })

    fig = px.bar(
        insights_df,
        x="Impact Score",
        y="Factor",
        orientation="h",
        title="Top Churn Drivers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

elif page == "High Risk Customers":

    st.title("⚠ High Risk Customers")

    high_risk_df = df[
        df["Contract"] == "Month-to-month"
    ]

    st.dataframe(
        high_risk_df.head(50),
        use_container_width=True
    )

    csv = high_risk_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download High Risk Customers",
        data=csv,
        file_name="high_risk_customers.csv",
        mime="text/csv"
    )

elif page == "Reports":

    st.title("📑 Reports")

    total_customers = len(df)

    churn_rate = (
        (df["Churn"] == "Yes").mean()
        * 100
    )

    revenue = df["MonthlyCharges"].sum()

    st.subheader("Executive Summary")

    st.write(
        f"""
        Total Customers: {total_customers:,}

        Churn Rate: {churn_rate:.2f}%

        Revenue: ${revenue:,.0f}
        """
    )

    st.markdown("### Recommendations")

    st.success(
        "Promote long-term contracts to reduce churn."
    )

    st.success(
        "Target low-tenure customers with retention campaigns."
    )

    st.success(
        "Encourage automatic payment methods."
    )

else:

    st.title("🤖 Predict Churn")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        senior = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        tenure = st.slider(
            "Tenure",
            0,
            72,
            12
        )

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        monthly_charges = st.number_input(
            "Monthly Charges",
            0.0,
            500.0,
            70.0
        )

        total_charges = st.number_input(
            "Total Charges",
            0.0,
            10000.0,
            500.0
        )

    with col2:

        st.subheader("Prediction Result")

        if st.button("Predict Churn"):

            customer = {
                "gender": gender,
                "SeniorCitizen": senior,
                "Partner": partner,
                "Dependents": dependents,
                "tenure": tenure,
                "PhoneService": phone_service,
                "InternetService": internet_service,
                "Contract": contract,
                "MonthlyCharges": monthly_charges,
                "TotalCharges": total_charges
            }

            result = predict_customer(
                customer
            )

            probability = result[
                "probability"
            ]

            if probability <= 40:
                risk = "Low"

            elif probability <= 70:
                risk = "Medium"

            else:
                risk = "High"

            st.metric(
                "Prediction",
                result["prediction"]
            )

            st.metric(
                "Probability",
                f"{probability}%"
            )

            st.metric(
                "Risk Level",
                risk
            )

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=probability,
                    title={
                        "text":
                        "Churn Risk"
                    },
                    gauge={
                        "axis": {
                            "range":
                            [0, 100]
                        }
                    }
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )