"""JTBD Skill 工具函数模块

提供知识库加载、文本处理、格式化输出等通用工具。
"""

from typing import Dict, List, Optional

from .config import KNOWLEDGE_BASE_DIR, KNOWLEDGE_FILES


def load_knowledge(topic: str) -> str:
    """加载指定主题的知识库内容。

    Args:
        topic: 主题标识符，对应 config.KNOWLEDGE_FILES 的键。
               可选值: theory, principles, forces, system, research,
               analysis, innovation, business, cases, models, reference

    Returns:
        知识库文件的完整文本内容。

    Raises:
        KeyError: 当 topic 不在已知主题列表中时。
        FileNotFoundError: 当知识库文件不存在时。
    """
    if topic not in KNOWLEDGE_FILES:
        available = ", ".join(sorted(KNOWLEDGE_FILES.keys()))
        raise KeyError(f"未知主题 '{topic}'，可选主题: {available}")

    file_path = KNOWLEDGE_BASE_DIR / KNOWLEDGE_FILES[topic]
    if not file_path.exists():
        raise FileNotFoundError(f"知识库文件不存在: {file_path}")

    return file_path.read_text(encoding="utf-8")


def load_all_knowledge() -> Dict[str, str]:
    """加载全部知识库内容。

    Returns:
        字典，键为主题标识符，值为对应文件内容。
    """
    result: Dict[str, str] = {}
    for topic in KNOWLEDGE_FILES:
        try:
            result[topic] = load_knowledge(topic)
        except FileNotFoundError:
            result[topic] = ""
    return result


def search_knowledge(keyword: str, topics: Optional[List[str]] = None) -> Dict[str, List[str]]:
    """在知识库中搜索包含关键词的段落。

    Args:
        keyword: 搜索关键词。
        topics: 限定搜索的主题列表，为 None 时搜索全部。

    Returns:
        字典，键为主题标识符，值为包含关键词的段落列表。
    """
    search_topics = topics if topics else list(KNOWLEDGE_FILES.keys())
    results: Dict[str, List[str]] = {}

    for topic in search_topics:
        try:
            content = load_knowledge(topic)
        except (KeyError, FileNotFoundError):
            continue

        paragraphs = content.split("\n\n")
        matched = [p.strip() for p in paragraphs if keyword.lower() in p.lower()]
        if matched:
            results[topic] = matched

    return results


def extract_sections(content: str, level: int = 2) -> Dict[str, str]:
    """从 Markdown 文本中按标题级别提取章节。

    Args:
        content: Markdown 文本内容。
        level: 标题级别（2 表示 ##，3 表示 ###）。

    Returns:
        字典，键为标题文本，值为该章节的正文内容。
    """
    prefix = "#" * level + " "
    sections: Dict[str, str] = {}
    current_title: Optional[str] = None
    current_lines: List[str] = []

    for line in content.split("\n"):
        if line.startswith(prefix):
            if current_title is not None:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = line[len(prefix):].strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections[current_title] = "\n".join(current_lines).strip()

    return sections


def format_as_markdown(title: str, sections: Dict[str, str], level: int = 2) -> str:
    """将结构化内容格式化为 Markdown 文档。

    Args:
        title: 文档标题。
        sections: 章节字典，键为章节标题，值为章节内容。
        level: 章节标题级别。

    Returns:
        格式化的 Markdown 字符串。
    """
    prefix = "#" * level
    parts = [f"# {title}\n"]
    for section_title, body in sections.items():
        parts.append(f"{prefix} {section_title}\n\n{body}\n")
    return "\n".join(parts)


def format_as_json(data: dict) -> str:
    """将字典格式化为缩进的 JSON 字符串。"""
    import json
    return json.dumps(data, ensure_ascii=False, indent=2)


def format_list(items: List[str], numbered: bool = False) -> str:
    """将列表格式化为 Markdown 列表文本。

    Args:
        items: 列表项。
        numbered: 是否使用有序列表。

    Returns:
        格式化的列表字符串。
    """
    lines = []
    for i, item in enumerate(items, 1):
        prefix = f"{i}." if numbered else "-"
        lines.append(f"{prefix} {item}")
    return "\n".join(lines)
