import streamlit as st
import importlib
import os
import pkgutil

st.set_page_config(page_title="Introduction to Mathematical Finance", page_icon="💸")

st.title("💸 Introduction to Mathematical Finance - Interactive Simulations")

st.markdown("""
Welcome! 👋  
Explore **Mathematical Finance** concepts visually and interactively.

First, select a **chapter**, then choose a **simulation** to explore. 🚀
""")

# --- Detect available chapters ---
chapter_dirs = [d for d in os.listdir() if d.startswith("cap") and os.path.isdir(d)]

chapters = []
for d in chapter_dirs:
    try:
        info_module = importlib.import_module(f"{d}.chapter_info")
        chapter_info = info_module.CHAPTER_INFO
        chapter_info["path"] = d
        chapters.append(chapter_info)
    except Exception as e:
        st.warning(f"⚠️ Failed to load {d}: {e}")

# --- Handle navigation ---
if "selected_chapter" not in st.session_state:
    st.session_state.selected_chapter = None

# --- If no chapter selected yet ---
if not st.session_state.selected_chapter:
    st.subheader("📘 Choose a Chapter")
    for c in chapters:
        with st.container(border=True):
            st.markdown(f"### {c['title']}")
            st.markdown(c["description"])
            if st.button(f"➡️ Open {c['title']}", key=c["path"]):
                st.session_state.selected_chapter = c
                st.rerun()

else:
    # --- Display simulations of the selected chapter ---
    chapter = st.session_state.selected_chapter
    chapter_path = chapter["path"]

    st.sidebar.button("⬅️ Back to Chapters", on_click=lambda: st.session_state.update({"selected_chapter": None}))
    st.header(f"📘 {chapter['title']}")
    st.markdown(chapter["description"])
    st.divider()

    # --- Detect simulations ---
    apps = []
    for finder, name, ispkg in pkgutil.iter_modules([chapter_path]):
        if ispkg:  # Only include subfolders (simulations)
            app_path = f"{chapter_path}.{name}.app"
            try:
                app_module = importlib.import_module(app_path)
                apps.append({
                    "title": app_module.APP_INFO["title"],
                    "description": app_module.APP_INFO["description"],
                    "module": app_path
                })
            except Exception as e:
                st.warning(f"⚠️ Error loading {app_path}: {e}")

    if apps:
        selected_sim = st.selectbox("🎯 Choose a Simulation:", [a["title"] for a in apps])
        selected_app = next(a for a in apps if a["title"] == selected_sim)

        app_module = importlib.import_module(selected_app["module"])
        st.markdown(f"#### 🧮 {selected_app['title']}")
        st.markdown(selected_app["description"])
        st.divider()
        app_module.run()
    else:
        st.info("No simulations found in this chapter yet. 🚧")

st.sidebar.divider()
st.sidebar.markdown("Developed with 💙 by **Pedro Maltez**")
