import streamlit as st

st.set_page_config(page_title="Laundry Kiloan", page_icon="🧺", layout="centered")


def rupiah(x):
    return "Rp " + f"{x:,.0f}".replace(",", ".")

# ===== TAMPILAN (CSS) - bagian ini cuma untuk desain =====
st.markdown("""
<style>
.header {
    background:
        linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px) 0 0 / 22px 22px,
        linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px) 0 0 / 22px 22px,
        linear-gradient(135deg, #0b2545, #13678a);
    padding: 28px 24px 22px 24px; border-radius: 18px; color: white; margin-bottom: 24px;
    box-shadow: 0 0 22px rgba(0,229,255,0.25);
}
.flow {
    height: 3px; margin-top: 16px; border-radius: 3px;
    background: linear-gradient(90deg, transparent, #00e5ff, transparent) 0 0 / 200px 3px repeat-x;
    animation: flow 1.6s linear infinite;
}
@keyframes flow { to { background-position: 200px 0; } }
.led {
    display: inline-block; width: 10px; height: 10px; border-radius: 50%;
    background: #39ff14; box-shadow: 0 0 8px #39ff14; margin-right: 8px;
    animation: blink 1.2s ease-in-out infinite;
}
@keyframes blink { 50% { opacity: 0.25; box-shadow: none; } }
.status { font-size: 0.75rem; letter-spacing: 1px; opacity: 0.9; margin-bottom: 8px; }
@keyframes swing {
    from { transform: translateX(-50%) rotate(-90deg); }
    to   { transform: translateX(-50%) rotate(var(--a)); }
}
@keyframes glow {
    50% { box-shadow: 0 0 26px rgba(0,229,255,0.75); }
}
.header h1 { margin: 0; font-size: 1.7rem; font-weight: 700; color: white; }
.header p { margin: 6px 0 0 0; opacity: 0.85; font-size: 0.95rem; }

.card {
    background: rgba(128,128,128,0.10); border: 1px solid rgba(128,128,128,0.25);
    border-radius: 14px; padding: 14px 16px; margin-bottom: 10px;
}
.card .label { font-size: 0.8rem; opacity: 0.7; }
.card .value { font-size: 1.15rem; font-weight: 600; }

.total {
    background: linear-gradient(135deg, #2a9d8f, #43c59e);
    border-radius: 14px; padding: 18px 20px; color: white; margin-top: 6px;
    box-shadow: 0 0 14px rgba(0,229,255,0.45); animation: glow 2s ease-in-out infinite;
}
.total .label { font-size: 0.85rem; opacity: 0.9; }
.total .value { font-size: 1.8rem; font-weight: 700; }


.scale-wrap { text-align: center; }
.gauge {
    position: relative; width: 200px; height: 100px; margin: 10px auto 6px auto;
    border-radius: 100px 100px 0 0; overflow: hidden;
    background: linear-gradient(90deg, #2a9d8f, #f4c95d, #e76f51);
}
.needle {
    position: absolute; bottom: 0; left: 50%; width: 4px; height: 88px;
    background: #1b1b1b; border-radius: 4px; transform-origin: bottom center;
}
.pivot {
    position: absolute; bottom: -8px; left: 50%; width: 18px; height: 18px;
    margin-left: -9px; background: #1b1b1b; border-radius: 50%;
}
.scale-label { font-size: 1.3rem; font-weight: 700; }
.basket { text-align: center; line-height: 1.5; }
.basket .icon { font-size: 3rem; }
.basket .items { font-size: 1.3rem; }

/* ===== LATAR BELAKANG ELEKTRO ===== */
.stApp {
    color: #e8f1ff;
    background:
        radial-gradient(circle at 15% 10%, rgba(0,229,255,0.18), transparent 40%),
        radial-gradient(circle at 85% 90%, rgba(122,92,255,0.18), transparent 45%),
        linear-gradient(rgba(0,229,255,0.07) 1px, transparent 1px) 0 0 / 40px 40px,
        linear-gradient(90deg, rgba(0,229,255,0.07) 1px, transparent 1px) 0 0 / 40px 40px,
        #070b14;
    background-attachment: fixed;
    animation: drift 12s linear infinite;
}
@keyframes drift {
    to { background-position: 0 0, 0 0, 0 40px, 40px 0, 0 0; }
}
.stApp label, .stApp p, .stApp h3 { color: #e8f1ff !important; }

/* ===== PETIR LATAR BELAKANG ===== */
.stApp::before {
    content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><path d='M60 20 L35 70 h22 l-8 45 35-60 h-24 z' fill='%2300e5ff' fill-opacity='0.13'/><path d='M240 170 L215 220 h22 l-8 45 35-60 h-24 z' fill='%23f4c95d' fill-opacity='0.12'/><path d='M270 30 L258 55 h11 l-4 22 17-30 h-12 z' fill='%237a5cff' fill-opacity='0.15'/><path d='M110 235 L98 260 h11 l-4 22 17-30 h-12 z' fill='%2300e5ff' fill-opacity='0.12'/></svg>");
    animation: kilatlatar 4s ease-in-out infinite;
}
@keyframes kilatlatar { 50% { opacity: 0.45; } }

/* ===== MESIN CUCI ===== */
.mesin-wrap { position: relative; width: 220px; margin: 10px auto 22px auto; }
.mesin {
    background: linear-gradient(160deg, #f5f9ff, #c9d8ea); border-radius: 18px; padding: 14px;
    box-shadow: 0 0 26px rgba(0,229,255,0.55);
}
.panel { display: flex; gap: 8px; align-items: center; height: 26px;
    border-bottom: 2px solid #9fb3c8; margin-bottom: 12px; }
.knob { width: 16px; height: 16px; border-radius: 50%; background: #0b2545; }
.lampu { margin-left: auto; width: 10px; height: 10px; border-radius: 50%;
    background: #39ff14; box-shadow: 0 0 8px #39ff14; animation: blink 1.2s ease-in-out infinite; }
.pintu { position: relative; width: 150px; height: 150px; margin: 0 auto 4px auto;
    border-radius: 50%; border: 9px solid #8fa7c0; overflow: hidden;
    background: radial-gradient(circle, #1d6fa5, #0b2545); box-shadow: inset 0 0 18px #000; }
.drum { position: absolute; inset: 0; animation: putar 1.3s linear infinite; }
.baju { position: absolute; width: 58px; height: 58px;
    clip-path: polygon(0% 20%, 25% 0%, 38% 8%, 62% 8%, 75% 0%, 100% 20%, 85% 40%, 75% 33%, 75% 100%, 25% 100%, 25% 33%, 15% 40%); }
.c1 { background: #ff6b6b; top: 44px; left: 14px; transform: rotate(-20deg); }
.c2 { background: #f4c95d; top: 30px; left: 48px; transform: rotate(15deg); }
.c3 { background: #43c59e; top: 62px; left: 34px; transform: rotate(-5deg); }
.c4 { background: #7a5cff; top: 70px; left: 66px; transform: rotate(25deg); }
.c5 { background: #ffffff; top: 50px; left: 60px; transform: rotate(-30deg); }
.c6 { background: #00b4ff; top: 78px; left: 10px; transform: rotate(12deg); }
.c7 { background: #ff9f43; top: 20px; left: 22px; transform: rotate(30deg); }
@keyframes putar { to { transform: rotate(360deg); } }
.bolt { position: absolute; font-size: 34px; filter: drop-shadow(0 0 8px #f4c95d);
    animation: kilat 1.5s ease-in-out infinite; }
.b1 { left: -44px; top: 18px; } .b2 { right: -44px; top: 18px; animation-delay: 0.4s; }
.b3 { left: -40px; top: 130px; animation-delay: 0.8s; } .b4 { right: -40px; top: 130px; animation-delay: 1.1s; }
@keyframes kilat {
    0%, 100% { opacity: 0.35; transform: scale(0.9) rotate(-8deg); }
    50% { opacity: 1; transform: scale(1.15) rotate(8deg); }
}

/* ===== TOMBOL ===== */
div.stButton { width: 100%; }
div.stButton > button {
    width: 100%; border-radius: 12px; padding: 12px 0; font-weight: 700;
    border: 1px solid rgba(0,229,255,0.5); background: rgba(0,229,255,0.08);
    color: #e8f1ff; transition: all 0.2s ease;
}
div.stButton > button:hover {
    box-shadow: 0 0 16px rgba(0,229,255,0.6); transform: translateY(-2px);
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #00b4ff, #7a5cff); border: none; color: white;
}
div.stTextInput input:focus, div.stNumberInput input:focus {
    box-shadow: 0 0 12px rgba(0,229,255,0.6);
}
</style>
""", unsafe_allow_html=True)

MESIN = """<div class="mesin-wrap">
<span class="bolt b1">⚡</span><span class="bolt b2">⚡</span>
<span class="bolt b3">⚡</span><span class="bolt b4">⚡</span>
<div class="mesin">
<div class="panel"><span class="knob"></span><span class="knob"></span><span class="lampu"></span></div>
<div class="pintu"><div class="drum">
<span class="baju c1"></span><span class="baju c2"></span><span class="baju c3"></span>
<span class="baju c4"></span><span class="baju c5"></span>
<span class="baju c6"></span><span class="baju c7"></span>
</div></div>
</div>
</div>"""

# ===== HEADER =====
st.markdown("""
<div class="header">
    <h1>⚡ Laundry Kiloan</h1>
    <p>Hitung cepat biaya laundry kiloan</p>
    <div class="flow"></div>
</div>
""", unsafe_allow_html=True)

# ===== INPUT =====
nim = st.text_input("NIM (10 digit)", key="nim", placeholder="contoh: 2411001347")
berat = st.number_input("Berat Cucian (kg)", key="berat", value=None, step=1,
                        placeholder="contoh: 10")


def reset():
    st.session_state.nim = ""
    st.session_state.berat = None


col1, col2 = st.columns(2)
hitung = col1.button("Hitung", type="primary")
col2.button("Reset", on_click=reset)

# ===== PROSES (logika tidak berubah) =====
if hitung:
    if len(nim) != 10 or not nim.isdigit():
        st.error("NIM tidak valid! Harus 10 digit angka.")
    elif berat is None or berat <= 0:
        st.error("Berat tidak valid! Harus bilangan bulat lebih dari 0.")
    else:
        tarif = 5000 + int(nim[-1]) * 500
        genap = 0
        for d in nim:
            if int(d) % 2 == 0:
                genap = genap + 1
        diskon = genap  # persen
        normal = berat * tarif
        potongan = diskon / 100 * normal
        total = normal - potongan

        # ===== MESIN CUCI =====
        st.markdown(MESIN, unsafe_allow_html=True)

        # ===== HASIL =====
        st.markdown("### Rincian Perhitungan")
        a, b = st.columns(2)
        a.markdown(f"""<div class="card"><div class="label">Tarif per kg</div>
            <div class="value">{rupiah(tarif)}</div></div>""", unsafe_allow_html=True)
        b.markdown(f"""<div class="card"><div class="label">Persen diskon</div>
            <div class="value">{diskon} %</div></div>""", unsafe_allow_html=True)
        c, d_ = st.columns(2)
        c.markdown(f"""<div class="card"><div class="label">Biaya normal</div>
            <div class="value">{rupiah(normal)}</div></div>""", unsafe_allow_html=True)
        d_.markdown(f"""<div class="card"><div class="label">Potongan</div>
            <div class="value">{rupiah(potongan)}</div></div>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="total"><div class="label">Total bayar</div>
            <div class="value">{rupiah(total)}</div></div>""", unsafe_allow_html=True)
