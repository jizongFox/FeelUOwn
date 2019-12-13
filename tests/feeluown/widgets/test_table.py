import time

import pytest

from tests.helpers import is_travis_env
from feeluown.widgets.table_meta import TableMetaWidget


# TODO: use xvfb in travis env
# example: https://github.com/pytest-dev/pytest-qt/blob/master/.travis.yml
@pytest.mark.skipif(is_travis_env, reason="travis env has no display")
def test_table_meta(qtbot):
    widget = TableMetaWidget()
    widget.title = '我喜欢的音乐'
    widget.subtitle = '嘿嘿'
    widget.creator = 'cosven'
    widget.updated_at = time.time()
    widget.desc = "<pre><code>print('hello world')</code><pre>"

    qtbot.addWidget(widget)
