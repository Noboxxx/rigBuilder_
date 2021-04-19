from maya import cmds
from ..utils import logUtils


@logUtils.log
def setup_new_scene():
    cmds.file(new=True, force=True)
