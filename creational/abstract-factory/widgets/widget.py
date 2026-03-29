from MotifWidgetFactory import MotifWidgetFactory
from PresentationManagerWidgetFactory import PresentationManagerWidgetFactory

if __name__ == "__main__":
    motif_window = MotifWidgetFactory.create_window()
    motif_scrollbar = MotifWidgetFactory.create_scrollbar()

    pm_window = PresentationManagerWidgetFactory.create_window()
    pm_scrollbar = PresentationManagerWidgetFactory.create_scrollbar()

    # Motif
    print(motif_window.render())
    print(motif_window.resize())
    print(motif_scrollbar.render())
    print(motif_scrollbar.scroll())

    print("\n")

    # Presentation Manager
    print(pm_window.render())
    print(pm_window.resize())
    print(pm_scrollbar.render())
    print(pm_scrollbar.scroll())