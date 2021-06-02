import hou

from ..texture_map.texture_format import TextureFormat
from .engine_connector import EngineConnector
from .builder import RedshiftNetworkBuilder


class RedshiftConnector(EngineConnector):
    def __init__(self):
        super(RedshiftConnector, self).__init__()

    def isAvailable(self):
        return hou.nodeType(hou.ropNodeTypeCategory(), 'Redshift_ROP') is not None

    def id(self):
        return 'redshift:1'

    def name(self):
        return 'Redshift'

    def icon(self):
        icon_name = hou.nodeType(hou.ropNodeTypeCategory(), 'Redshift_ROP').icon()
        return hou.qt.Icon(icon_name, 16, 16)

    def nodeTypeAssociatedWithEngine(self, node_type):
        _, namespace, name, _ = node_type.nameComponents()

        if namespace.lower() == 'redshift':
            return True

        if isinstance(node_type, hou.VopNodeType) and 'redshift' in node_type.renderMask().lower():
            return True

        if name.lower().startswith('rs_'):
            return True

        if 'redshift' in name.lower():
            return True

        return False

    def builders(self):
        return RedshiftNetworkBuilder(self),

    def supportedTextureFormats(self):
        return TextureFormat.wrap('exr', 'ptx', 'ptex', 'hdr', 'png', 'tga', 'tif', 'tiff', 'jpg', 'jpeg', )


EngineConnector.registerEngine(RedshiftConnector)
