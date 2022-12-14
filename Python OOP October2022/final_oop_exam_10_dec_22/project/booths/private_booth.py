from final_oop_exam_10_dec_22.project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.5

    def reserve(self, number_of_people):
        self.price_for_reservation = PrivateBooth.PRICE_PER_PERSON * number_of_people
        self.is_reserved = True