# author: JalexCode
# Etecsa Banner


# STYLES ###############################################
STACKED_WIDGET_CSS = """QStackedWidget QToolButton::left-arrow:enabled {
	 image: url('ui/graphics/lil_back.png');
	/*image: url(:/graphics/lil_back.png);*/
 }
QStackedWidget QToolButton::right-arrow:enabled {
     image: url('ui/graphics/lil_forward.png');
	/*image: url(:/graphics/lil_forward.png);*/
 }"""
SCROLL_AREA_CSS = """
QAbstractScrollArea
{
    border-radius: 2px;
    /*border: 1px solid #76797C;*/
    background-color: transparent;
    color: white;
}

QScrollBar:horizontal
{
    height: 15px;
    margin: 3px 15px 3px 15px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
    background-color: #2A2929;
}

QScrollBar::handle:horizontal
{
    background-color: #605F5F;
    min-width: 5px;
    border-radius: 4px;
}

QScrollBar::add-line:horizontal
{
    margin: 0px 3px 0px 3px;
    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
    width: 10px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    margin: 0px 3px 0px 3px;
    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
{
    border-image: url(:/qss_icons/rc/right_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
{
    border-image: url(:/qss_icons/rc/left_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: #2A2929;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
}

QScrollBar::handle:vertical
{
    background-color: #605F5F;
    min-height: 5px;
    border-radius: 4px;
}

QScrollBar::sub-line:vertical
{
    margin: 3px 0px 3px 0px;
    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{
    margin: 3px 0px 3px 0px;
    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
{

    border-image: url(:/qss_icons/rc/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
{
    border-image: url(:/qss_icons/rc/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}"""
PROGRESS_BAR_STYLE = """QProgressBar {
    border: none;
    /*border-radius: 1px;*/
    text-align: center;
	background-color: transparent/*rgb(0, 0, 0);*/
}

QProgressBar::chunk {
    border-radius: 0.5px;
    background-color: red;
}"""
BANNER_NORMAL_CONTROL_BUTTONS_CSS = """background-color: rgb(64, 64, 64);
    /*border-top-left-radius: 10px;*/
    /*border-bottom-left-radius: 10px;*/
    border:none"""
BANNER_OVER_CONTROL_BUTTONS_CSS = """background-color: grey;
    /*border-top-left-radius: 10px;*/
    /*border-bottom-left-radius: 10px;*/
    border:none"""
DETAILED_IMAGE_LABEL = """color:white;
    background-color: rgba (0, 0, 0, 80);
    font: 15pt 'Segoe UI';
    padding: 5px;"""