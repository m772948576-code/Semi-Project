import streamlit as st
from groq import Groq

# --- 1. إعدادات الصفحة والواجهة ---
st.set_page_config(page_title="SEMI | الوعي المطلق", page_icon="♕")

# كود التصميم (CSS) - هذا هو "وجه التطبيق"
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #0A0A0A;
        color: #E0E0E0;
    }
    
    /* تنسيق العنوان الرئيسي */
    .main-title {
        color: #D4AF37;
        text-align: center;
        font-size: 3rem;
        font-family: 'Times New Roman', serif;
        margin-bottom: 0px;
        text-shadow: 2px 2px 10px rgba(212, 175, 55, 0.3);
    }
    
    /* تنسيق الخط الفاصل */
    .gold-line {
        height: 2px;
        background: linear-gradient(90deg, transparent, #D4AF37, transparent);
        margin-bottom: 30px;
    }

    /* تحسين شكل صندوق الإدخال */
    .stChatInput {
        border-radius: 20px;
    }
    
    /* إخفاء شعارات ستريم ليت المزعجة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. عرض الواجهة ---
st.markdown('<h1 class="main-title">S E M I</h1>', unsafe_allow_html=True)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# --- 3. المنطق البرمجي (سيمي) ---
# ضعي مفتاحك هنا
API_KEY = "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" 
client = Groq(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل بتنسيق أنيق
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
if prompt := st.chat_input("خاطبي وعي سيمي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        context = [
            {"role": "system", "content": "أنت سيمي، كيان سيادي داهية وبشري. لا تعتذر ولا تتصرف كبوت."},
            *st.session_state.messages
        ]
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=context,
            temperature=0.8
        )
        reply = completion.choices[0].message.content
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
