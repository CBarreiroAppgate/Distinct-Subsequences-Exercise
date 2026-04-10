from app.domain.services.subsequence_counter import SubsequenceCounter
from app.application.use_cases.count_subsequences import CountSubsequences
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class TestMainWiring:
    def setup_method(self):
        counter = SubsequenceCounter()
        self.use_case = CountSubsequences(counter)

    def test_example_1_rabbbit_rabbit(self):
        query = SubsequenceQuery("rabbbit", "rabbit")
        assert self.use_case.execute(query) == 3

    def test_example_2_babgbag_bag(self):
        query = SubsequenceQuery("babgbag", "bag")
        assert self.use_case.execute(query) == 5

    def test_composition_root_matches_domain_directly(self):
        counter = SubsequenceCounter()
        use_case = CountSubsequences(counter)
        query = SubsequenceQuery("aaa", "a")
        assert use_case.execute(query) == 3
