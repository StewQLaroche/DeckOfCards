

class Card():

    def __init__(self, suite=None, face=None, public_hidden=False, private_hidden=False, joker=False):

        self.joker = joker

        self.suite = suite
        self.face = face

        self.public_hidden = public_hidden
        self.private_hidden = private_hidden

    def reveal_to_public(self):
        self.public_hidden = False

    def reveal_to_owner(self):
        self.private_hidden = False

    def hide_from_public(self):
        self.public_hidden = True

    def hide_from_owner(self):
        self.private_hidden = True

    def get_card_info(self, view_type="private"):

        if view_type not in ["private", "public"]:
            view_type = "private"

        if (view_type == "private" and not self.private_hidden) or (view_type == "public" and not self.public_hidden):

            if self.joker:
                return "Joker", "Joker"

            return self.face, self.suite

        else:
            return None, None
