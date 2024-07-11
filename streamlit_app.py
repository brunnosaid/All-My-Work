import streamlit as st

def main():
    st.title("Redirecionamento para Links")
    
    # Criação dos botões para os links
    if st.button("CyberSecurity"):
        st.markdown("[TryHackMe](https://tryhackme.com/p/AsherAxe23)")
        st.markdown("[PicoCTF](https://play.picoctf.org/users/Ash3rAx3)")
    
    if st.button("Social Media"):
        st.markdown("[Instagram](https://www.instagram.com/brunnosaid)")
        st.markdown("[FaceBook](https://www.facebook.com/brunnosaid)")
        st.markdown("[TwitchTV](https://www.twitchtv.com/brunnosaid)")
    
    if st.button("Donate"):
        st.markdown("[QR Code](https://github.com)")

if __name__ == "__main__":
    main()
