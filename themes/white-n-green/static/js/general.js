window.WOS = window.WOS || {};

WOS.UI = {
    init: function init() {
        this.DOM.init();
    },
    DOM: {
        $linkCollection : null,
        init: function init() {
            var WUI = WOS.UI;
            
            if(!WOS.Helpers.isSmall()) {
                WUI.DOM.$linkCollection  = $('img.alignnone, img.alignleft, img.alignright, img.aligncenter').parent();
                WUI.DOM.alterLinks();
                WUI.Helpers.applyColorBox();
            }
        },
        alterLinks: function alterLinks(){
            var $links = WOS.UI.DOM.$linkCollection;
            if ($links !== null && $links.length >0) {
                WOS.UI.DOM.addRels($links);
                WOS.UI.DOM.addTitles($links);
            }
        },
        addRels: function addRels($links) {
            $links.attr('rel','grouped');
        },
        addTitles: function addTitles($links) {
            $links.each(function() {
                var $this = $(this), $child = $this.children('img');
                $this.attr('title', $.trim($child.attr('alt')));
            });
        }
    },
    Helpers: {
        applyColorBox: function applyColorBox() {
            var $links =  window.WOS.UI.DOM.$linkCollection;
            if ($links !== null && $links.length >0)
                $links.colorbox({'maxWidth': '1000px'});
        }
    }
};

WOS.Helpers = {
    isSmall: function isSmall(){
        return $(window).width() <= 640;
    }
};