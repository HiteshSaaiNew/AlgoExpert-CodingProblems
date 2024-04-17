from collections import defaultdict


class Solution:
    def tournamentWinner1(self, competitions, results):
        # Time O(n) || Space O(k)
        # n - no.of.competition k - no.of.teams

        if len(results) != len(competitions):
            return ""

        teams = defaultdict(int)

        for i in range(0, len(competitions)):

            if results[i] == 0:
                teams[competitions[i][1]] += 3

            else:
                teams[competitions[i][0]] += 3

        return max(teams, key=teams.get)

    def tournamentWinner2(self, competitions, results):
        # Time O(n) || Space O(k)
        # n - no.of.competition k - no.of.teams
        if len(results) != len(competitions):
            return ""

        teams = defaultdict(int)
        currentBestTeam = ""
        teams[currentBestTeam] = 0

        for i in range(0, len(competitions)):
            homeTeam, awayTeam = competitions[i]

            winningTeam = awayTeam if results[i] == 0 else homeTeam
            teams[winningTeam] += 3
            if teams[winningTeam] > teams[currentBestTeam]:
                currentBestTeam = winningTeam

        return currentBestTeam


if __name__ == "__main__":

    print("Winned of the First Tournament!!")
    print(
        Solution().tournamentWinner1(
            [
                ["Bulls", "Eagles"],
                ["Bulls", "Bears"],
                ["Bulls", "Monkeys"],
                ["Eagles", "Bears"],
                ["Eagles", "Monkeys"],
                ["Bears", "Monkeys"],
            ],
            [1, 1, 1, 1, 1, 1],
        )
    )

    print("Winned of the Second Tournament!!")
    print(
        Solution().tournamentWinner2(
            [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1]
        )
    )
