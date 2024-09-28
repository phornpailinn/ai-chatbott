import streamlit as st
import google.generativeai as genai

# App title
st.title("🦁 Explore the Zoo: Chat with Us!")

# Input for Gemini API Key
gemini_api_key = "AIzaSyAPjp1uXJVHrSnv9cRJ0GGEMCLnhlCz5w4"

# Authenticate the API if the user provides a key
if gemini_api_key:
    try:
        # Configure the API with the provided key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")  # ใช้โมเดล Gemini สำหรับการตอบสนอง
        st.success("Gemini API Key ตั้งค่าเรียบร้อยแล้ว.")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดขณะตั้งค่า Gemini model: {e}")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Dictionary of zoo information for various zoos
zoo_info = {
    "สวนสัตว์ดุสิต": "สวนสัตว์ดุสิตตั้งอยู่ในกรุงเทพฯ มีสัตว์หลากหลายชนิด เช่น ช้าง เสือ และยีราฟ เปิดตั้งแต่ 08:00 น. ถึง 18:00 น.",
    "สวนสัตว์เปิดเขาเขียว": "สวนสัตว์เปิดเขาเขียวที่ชลบุรี เป็นสวนสัตว์เปิดที่คุณสามารถขับรถชมสัตว์อย่างใกล้ชิด เปิดตั้งแต่ 08:00 น. ถึง 18:00 น.",
    "สวนสัตว์เชียงใหม่": "สวนสัตว์เชียงใหม่ มีหมีแพนด้าที่น่ารัก และสัตว์นานาชนิด เปิดตั้งแต่ 08:00 น. ถึง 17:00 น.",
    "ซาฟารีเวิลด์": "ซาฟารีเวิลด์ในกรุงเทพฯ มีโซนซาฟารีปาร์คและมารีนปาร์ค เปิดทุกวันตั้งแต่ 09:00 น. ถึง 17:00 น.",
    "สวนสัตว์นครราชสีมา": "สวนสัตว์นครราชสีมามีสัตว์หายาก เช่น แรดอินเดีย เปิดตั้งแต่ 08:00 น. ถึง 18:00 น."
}

# Function to respond based on keywords
def get_zoo_info(user_input):
    user_input_lower = user_input.lower()
    
    if "ดุสิต" in user_input_lower:
        return zoo_info["สวนสัตว์ดุสิต"]
    elif "เขาเขียว" in user_input_lower:
        return zoo_info["สวนสัตว์เปิดเขาเขียว"]
    elif "เชียงใหม่" in user_input_lower:
        return zoo_info["สวนสัตว์เชียงใหม่"]
    elif "ซาฟารีเวิลด์" in user_input_lower:
        return zoo_info["ซาฟารีเวิลด์"]
    elif "นครราชสีมา" in user_input_lower:
        return zoo_info["สวนสัตว์นครราชสีมา"]
    else:
        return "ขออภัยค่ะ บอทไม่เข้าใจคำถามนี้ กรุณาถามเกี่ยวกับสวนสัตว์ดุสิต, สวนสัตว์เปิดเขาเขียว, สวนสัตว์เชียงใหม่, ซาฟารีเวิลด์ หรือสวนสัตว์นครราชสีมาได้ค่ะ."

# Input for user message
user_input = st.text_input("สอบถามเกี่ยวกับสวนสัตว์ต่างๆ ได้ที่นี่:")

# Add user input to chat history without displaying it
if user_input:
    st.session_state.chat_history.append(("user", user_input))

    # Check if API Key is provided and model is set up
    if gemini_api_key and model:
        try:
            # Generate AI-based response
            response = model.generate_content(user_input)
            bot_response = response.text
            st.session_state.chat_history.append(("assistant", bot_response))
            st.write(f"**AI บอท:** {bot_response}")
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดขณะสร้างคำตอบ AI: {e}")
    
    else:
        # Use predefined zoo information if no AI response
        bot_response = get_zoo_info(user_input)
        
        # Append bot response to chat history without displaying it
        st.session_state.chat_history.append(("assistant", bot_response))
        st.write(f"**บอท:** {bot_response}")


