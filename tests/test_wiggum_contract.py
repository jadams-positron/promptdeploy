from pathlib import Path
import unittest
R=Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_skill(self):
  t=(R/'skills/wiggum/SKILL.md').read_text(); self.assertIn('sole root',t); self.assertIn('two total repair rounds',t); self.assertIn('one risk-appropriate final review',t); self.assertNotIn('Audit that commit',t)
 def test_command(self): self.assertIn('Do not run this command from another skill',(R/'commands/wiggum.md').read_text())
 def test_audit(self):
  t=(R/'skills/wiggum/references/fess-audit.md').read_text(); self.assertIn('at most once',t); self.assertIn('Do not audit every commit',t)
if __name__=='__main__': unittest.main()
