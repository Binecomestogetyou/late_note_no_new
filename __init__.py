from aqt import mw
from aqt import gui_hooks


def block_new() -> None:

    if mw.col.find_cards("is:due -prop:due=0"):
        for card in mw.col.find_cards("is:due -prop:due=0"):
            deck_name = mw.col.decks.name(mw.col.get_card(card).did)
            query_str = "deck:\"" + deck_name + "\" is:new"
            mw.col.sched.set_due_date(mw.col.find_cards(query_str), "1")


gui_hooks.main_window_did_init.append(block_new)
