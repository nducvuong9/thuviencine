import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
from resources.lib import search, movies, tvshows, categories

_url = sys.argv[0]
_handle = int(sys.argv[1])
_addon = xbmcaddon.Addon()

if sys.version_info.major == 2:
    from urlparse import parse_qsl
else:
    from urllib.parse import parse_qsl

def main_menu():
    xbmcplugin.addDirectoryItem(_handle, f"{_url}?action=search", xbmcgui.ListItem("Tìm kiếm"), True)
    xbmcplugin.addDirectoryItem(_handle, f"{_url}?action=movies", xbmcgui.ListItem("Phim lẻ"), True)
    xbmcplugin.addDirectoryItem(_handle, f"{_url}?action=tvshows", xbmcgui.ListItem("Phim bộ"), True)
    xbmcplugin.addDirectoryItem(_handle, f"{_url}?action=categories", xbmcgui.ListItem("Phân loại"), True)
    xbmcplugin.endOfDirectory(_handle)

def router(paramstring):
    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'search':
            search.search()
        elif params['action'] == 'movies':
            movies.list_movies()
        elif params['action'] == 'tvshows':
            tvshows.list_tvshows()
        elif params['action'] == 'categories':
            categories.list_categories()
    else:
        main_menu()

if __name__ == '__main__':
    router(sys.argv[2][1:])