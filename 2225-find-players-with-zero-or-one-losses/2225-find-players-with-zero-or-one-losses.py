
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0

            losses[loser] = losses.get(loser, 0) + 1

        zero_losses = []
        one_loss = []

        for player, count in losses.items():
            if count == 0:
                zero_losses.append(player)
            elif count == 1:
                one_loss.append(player)

        zero_losses.sort()
        one_loss.sort()

        return [zero_losses, one_loss]
