from docutils.core import publish_parts
from docutils.writers.html4css1 import Writer
import rst_pygments

# thx to zerok and bartTC
def make_rst(text):
    rst = publish_parts(
        text,
        settings_overrides={
            'initial_header_level': 2,
            'doctitle_xform': False,
            'footnote_references': 'superscript',
            'trim_footnote_reference_space': True,
            'default_reference_context': 'view',
            'link_base': '',
        },
        writer=Writer())
    return rst['body']
