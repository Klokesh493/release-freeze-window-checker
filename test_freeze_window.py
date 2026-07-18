import unittest

from freeze_window import evaluate


class FreezeWindowTest(unittest.TestCase):
    def test_blocks_tier1_late_deploy(self):
        rows = [{"service": "storefront", "tier": "tier1", "deploy_time": "2026-07-18T23:10:00", "freeze_start": "2026-07-18T18:00:00", "freeze_end": "2026-07-18T23:59:00"}]
        self.assertEqual(evaluate(rows)[0]["decision"], "block")


if __name__ == "__main__":
    unittest.main()
