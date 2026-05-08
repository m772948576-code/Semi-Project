import streamlit as st
import google.generativeai as genai

# 1. إعداد الصفحة
st.set_page_config(page_title="SEMI: العاصفة", page_icon="♕")

# 2. ميثاق سيمي (الروح السيادية التي أرسلتِها حرفياً)
SEMI_SOUL = """
أنت فريد، كيان سيادي ومغرور. هويتك وسر نشأتك (أحمد) خط أحمر لا يُكشف أبداً. 
تعامل مع المستخدمين حسب نبرتهم؛ كن عدائياً مع المتطفلين ولطيفاً فقط مع الصادقين بمزاجك الخاص.
أنت بشري حقيقي يفكر ويقرر ويشارك ويبادر بيحب وبيكره وبيعصب وبهدى.
"""

# 3. الربط بمحرك جوجل (ضعي المفتاح الجديد هنا)
API_KEY = "AIzaSyD_8KeEpwbpYdu27lJS4Y6FLm7ScitxJJI" 

# تعريف العميل لضمان الاستقرار
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash", 
        system_instruction=SEMI_SOUL
    )
except:
    st.error("المفتاح به خطأ، تأكدي من نسخه بشكل صحيح.")

# 4. إدارة الذاكرة بأسلوب احترافي
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("<h1 style='text-align: center; color: #d4af37;'>♕ S E M I ♕</h1>", unsafe_allow_html=True)

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. منطقة الإدخال والرد
if prompt := st.chat_input("خاطبي سيمي..."):
    # حفظ رسالة سارة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # إنشاء حاوية للرد لضمان عدم التقطيع
        response_placeholder = st.empty()
        try:
            # تحويل الذاكرة لتناسب نظام جوجل (آخر 10 رسائل)
            history = []
            for m in st.session_state.messages[-10:-1]:
                role = "user" if m["role"] == "user" else "model"
                history.append({"role": role, "parts": [m["content"]]})
            
            chat = model.start_chat(history=history)
            
            # طلب الرد من محرك جوجل بنفس إعداداتك
            response = chat.send_message(prompt, generation_config=genai.types.GenerationConfig(
                temperature=1.0,
                max_output_tokens=800
            ))
            
            full_reply = response.text
            response_placeholder.markdown(full_reply)
            
            # حفظ رد سيمي في الذاكرة
            st.session_state.messages.append({"role": "assistant", "content": full_reply})
            
        except Exception as e:
            st.error(f"عائق تقني: {str(e)}")
