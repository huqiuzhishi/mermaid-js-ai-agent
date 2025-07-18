import llm
from dotenv import load_dotenv
import os
from mako.template import Template

# Load environment variables from .env file
load_dotenv()


def conditional_render(prompt, context, start_delim="% if", end_delim="% endif"):
    template = Template(prompt)
    return template.render(**context)


def parse_markdown_backticks(str) -> str:
    if "```" not in str:
        return str.strip()
    # Remove opening backticks and language identifier
    str = str.split("```", 1)[-1].split("\n", 1)[-1]
    # Remove closing backticks
    str = str.rsplit("```", 1)[0]
    # Remove any leading or trailing whitespace
    return str.strip()


def prompt(model: llm.Model, prompt: str):
    res = model.prompt(prompt)
    return res.text()


def get_model_name(model: llm.Model):
    return model.model_id


def build_sonnet_3_5():
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    sonnet_3_5_model: llm.Model = llm.get_model("claude-3.5-sonnet")
    sonnet_3_5_model.key = ANTHROPIC_API_KEY

    return sonnet_3_5_model


def build_mini_model():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    gpt4_o_mini_model: llm.Model = llm.get_model("gpt-4o-mini")
    gpt4_o_mini_model.key = OPENAI_API_KEY
    return gpt4_o_mini_model


def build_big_3_models():
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    sonnet_3_5_model: llm.Model = llm.get_model("claude-3.5-sonnet")
    sonnet_3_5_model.key = ANTHROPIC_API_KEY

    gpt4_o_model: llm.Model = llm.get_model("4o")
    gpt4_o_model.key = OPENAI_API_KEY

    gemini_2_5_flash_model: llm.Model = llm.get_model("gemini/gemini-2.5-flash")
    gemini_2_5_flash_model.key = GEMINI_API_KEY

    return gemini_2_5_flash_model


def build_latest_openai():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # chatgpt_4o_latest_model: llm.Model = llm.get_model("chatgpt-4o-latest") - experimental
    chatgpt_4o_latest_model: llm.Model = llm.get_model("gpt-4o-2024-08-06")
    chatgpt_4o_latest_model.key = OPENAI_API_KEY
    return chatgpt_4o_latest_model


def build_big_3_plus_mini_models():
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    sonnet_3_5_model: llm.Model = llm.get_model("claude-3.5-sonnet")
    sonnet_3_5_model.key = ANTHROPIC_API_KEY

    gpt4_o_model: llm.Model = llm.get_model("4o")
    gpt4_o_model.key = OPENAI_API_KEY

    gemini_2_5_flash_model: llm.Model = llm.get_model("gemini/gemini-2.5-flash")
    gemini_2_5_flash_model.key = GEMINI_API_KEY

    gpt4_o_mini_model: llm.Model = llm.get_model("gpt-4o-mini")
    gpt4_o_mini_model.key = OPENAI_API_KEY

    chatgpt_4o_latest_model = build_latest_openai()

    return (
        sonnet_3_5_model,
        gpt4_o_model,
        gemini_2_5_flash_model,
        gpt4_o_mini_model,
    )


def build_gemini_duo():
    gemini_1_5_pro: llm.Model = llm.get_model("gemini-1.5-pro-latest")
    gemini_1_5_flash: llm.Model = llm.get_model("gemini-1.5-flash-latest")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    gemini_1_5_pro.key = GEMINI_API_KEY
    gemini_1_5_flash.key = GEMINI_API_KEY

    return gemini_1_5_pro, gemini_1_5_flash
