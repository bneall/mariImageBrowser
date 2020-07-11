#
# MIBView Init
#

import os
import mari

import config
import utils

# Main Config Object
cfg = config.Config()

# Setup Constants
MIB_CONVERTERMAP = utils.getConverterPlugins(cfg.converterPath)
MIB_STYLESHEET = utils.getStyleSheet(cfg.resourcePath)
MIB_FORMATS = mari.images.supportedReadFormats()

# Load Mari Config
mariConfPath = os.path.normpath(os.path.join(mari.resources.path(mari.resources.USER), 'mib.conf'))
if cfg.loadConfig(mariConfPath):
    utils.info('Loading local config')
elif cfg.saveConfig(mariConfPath):
    utils.info('Loading default config')
else:
    utils.warn('Could not save config, settings will not be saved!')

# Force update configs converters
# to keep in step with converters available on disk.
cfg.set_converters(MIB_CONVERTERMAP.keys())

#-------------------------------------------
def launch():
    try:
        import ui

        tabName = 'Image Browser'

        # Clean Up
        try:
            mari.app.removeTab(tabName)
        except:
            pass

        global mibviewwdg
        mibviewwdg = ui.MIBView()
        mari.app.addTab(tabName, mibviewwdg)

    except:
        utils.error('Initialization failed.')
        raise
