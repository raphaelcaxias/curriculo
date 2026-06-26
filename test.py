import sys
print(f"Python: {sys.version}")

try:
    import streamlit
    print(f"✅ Streamlit {streamlit.__version__}")
except Exception as e:
    print(f"❌ {e}")

try:
    import pandas
    print(f"✅ Pandas {pandas.__version__}")
except Exception as e:
    print(f"❌ {e}")

try:
    import plotly
    print(f"✅ Plotly {plotly.__version__}")
except Exception as e:
    print(f"❌ {e}")
