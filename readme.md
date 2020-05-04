# NBA Statistic Stabilization

### Motivation
As the first few weeks of each NBA season unfold many analysts are quick to draw conclusions from early-season results. But what if, due to small sample size, it's too early in the season to jump to conclusions? More importantly, when can we actually start drawing conclusions about a team's shooting ability.

The goal of this project is to determine how many games into a season it takes for a given statistic to 'stabilize'. In other words, how far into the season before we can trust a team's ability in a given metric.


### Data
There are two datasets in the `data` directory both of which were scraped from Basketball-Reference.com. The `games.csv` file includes individual game statistics for all 30 NBA teams over the previous 10 seasons (2009-2010 through 2018-2019). One slight road bump to keep in mind is that the 2011-2012 season was truncated to 66 total games instead of 82. Each record includes an individual team's performance, mostly shooting metrics, on a game-by-game basis. The `seasons.csv` file includes each team's season-ending statistics or how they did in aggregate over the course of the season.

### Approaches
To help determine when a given statistic stabilizes, I calculated the correlation between each cumulative statistic up through each game number (1-82), found in the `games.csv` file, and the team's season-ending statistic in the `seasons.csv` file. A few alternative approaches are included in the references section.

### Findings
Two-point field goal percentage stabilizes first. You can get a relatively good feel for a team's ability to shoot from inside the arc after about 5 games. Although this may be saying more about their ability to generate high-value rim attempts as opposed to long-range 2's. Free throw percentage stabilizes next at around 10 games followed by three-point percentage around 20 games into the season.

![Shooting_Stabilization](/plots/Shooting_Stabilization.png)

To visualize the variance in these three metrics in addition to `FG%` on a game-by-game basis, I've included the distribution of each below.

![Game_FG%](/plots/Game_FG.png)

![Game_2PT%](/plots/Game_2PT.png)

![Game_3PT%](/plots/Game_3PT.png)

![Game_FT%](/plots/Game_FT.png)




### References
- [When Can We Trust a Team's Stats](https://fansided.com/2017/12/21/nylon-calculus-team-stats-noise-stabilization-thunder/)
- [How Long Does It Take for Three-Point Shooting To Stabilize](https://fansided.com/2014/08/29/long-take-three-point-shooting-stabilize/)
