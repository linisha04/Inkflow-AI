# Inkflow-AI
# InkFlowAI: Blog Creation Assistant 🤖

InkFlowAI is a powerful and user-friendly application designed to help users generate high-quality blog content effortlessly. With InkFlowAI, you can create creative blog titles and generate fully-structured blog posts with ease, making it an essential tool for content creators, bloggers, and marketers.

---

## Features

### 📚 **Generate Creative Blog Titles**
- Input a topic and get a list of 5 creative blog titles.
- Titles are tailored to be informative, humorous, or persuasive, targeting beginners, intermediates, or experts.

### 🖋️ **Generate High-Quality Blog Posts**
- Provide a blog title, keywords, and desired blog length.
- Content is structured with an introduction, body paragraphs, and a conclusion.
- Blogs are written in a conversational and engaging style, targeting a beginner audience.
- Includes specified keywords for SEO optimization.

### 📋 **Interactive Keyword Management**
- Add and manage keywords dynamically.
- Keywords are visually displayed to help users track their inputs.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building an interactive web-based interface.
- **LangChain**: To manage and structure prompt templates.
- **Hugging Face Hub**: To integrate with advanced LLMs like Meta-Llama and Mistral for blog generation.

---

## How It Works

1. **Blog Titles:**
   - Input a topic via the Streamlit interface.
   - Generate five creative blog titles using the Hugging Face LLM.

2. **Blog Post Generation:**
   - Provide a blog title, specify the desired blog length, and add keywords.
   - Generate a plagiarism-free, informative blog post that follows a well-structured format.

3. **Dynamic Keyword Management:**
   - Add keywords dynamically.
   - Keywords are displayed interactively for easy tracking.

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- A Hugging Face Hub API Key

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/linisha04/InkFlow-AI.git
   cd InkFlow-AI
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a file named `secret_key.py` and add your Hugging Face Hub API key:
   ```python
   api_key = "your_huggingface_api_key"
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Access the App**
   Open your browser and go to: `http://localhost:8501`

---

## Usage

1. Use the **"Generate Creative Blog Titles"** section to create blog titles by entering a topic.
2. Use the **"Generate Blog Post"** section to:
   - Enter a blog title and specify the desired length.
   - Add keywords dynamically.
   - Generate a complete blog post.

---

## Example Workflow

1. **Input Topic:** "Artificial Intelligence in Education"
2. **Generated Titles:**
   - Title 1: "How AI is Transforming Modern Education"
   - Title 2: "5 Ways AI is Revolutionizing Learning for Beginners"
   - Title 3: "The Role of Artificial Intelligence in Personalized Education"
   - Title 4: "AI in Education: What Every Teacher Should Know"
   - Title 5: "Exploring the Future of AI-Powered Classrooms"

3. **Blog Post Details:**
   - Title: "How AI is Transforming Modern Education"
   - Keywords: "AI, education, learning"
   - Length: 500 words

4. **Generated Blog:**
   A complete, engaging blog post with an introduction, body paragraphs, and conclusion.

---

## Future Enhancements

- Add support for more advanced customization (e.g., tone, style).
- Expand keyword management features.
- Include additional LLM models for more diverse writing styles.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Hugging Face Hub for the advanced LLM integration.
- LangChain for prompt management.
- Streamlit for an interactive and intuitive interface.

---

Start creating amazing blogs with **InkFlowAI** today!

