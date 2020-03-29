# Monster Hunter World Optimizer

This repository maintains a program used as a tool to optimize a player's equipment loadout in
[Monster Hunter World](https://www.monsterhunterworld.com). This is a side project that's improved
every once in a while when I personally need it improved. Normally improvements are such that
they're _just enough_ to serve whatever new need I have.

The application takes a list of equipment pieces, generates all possible valid combinations of them,
and then scores and filters them based on a configuration, outputting a file with the highest scored
combinations.

## How To

Read on for quick instructions on using the application.

### Running the Application

To run the application, run the following command:

```shell script
$ python main.py <equipment CSV> <combination output file> <JSON config>
```

### Examples

If you just want to get a quick idea on your own for how to use this, take a look at the
[example_data](https://github.com/leodenault/mhw_optimizer/tree/master/example_data) directory.
Otherwise read on for more details.

### Gathering Data

The application requires 2 files to run:

*   Equipment data
*   A JSON configuration

#### Equipment Data

The application does not automatically fetch or supply equipment information. Instead it relies on
a CSV file that supplies equipment data. Since the application brute forces the combinations, it is
**highly recommended** to reduce the provided equipment as much as possible to avoid creating too
many combinations in memory.

The CSV file should dedicate the first row to headers. Headers are:

Header                       | Description                                              | Required?
---------------------------- | -------------------------------------------------------- | :-------:
Equipment Piece Name         | The name of the equipment piece as defined in the game   | Yes
Skill 1 Name                 | The name of the first skill associated with the piece    | Yes
Skill 1 Level                | The level of the first skill                             | Yes
Skill 2 Name                 | The name of the second skill associated with the piece   | No
Skill 2 Level                | The level of the second skill                            | No
Num Lvl 1 Deco Slots         | The number of level 1 decoration slots on the piece      | Yes
Num Lvl 2 Deco Slots         | The number of level 2 decoration slots on the piece      | Yes
Num Lvl 3 Deco Slots         | The number of level 3 decoration slots on the piece      | Yes
Num Lvl 4 Deco Slots         | The number of level 4 decoration slots on the piece      | Yes
Body Part                    | The body part covered by the equipment piece. Valid options are:<br><ul><li>Head<li>Body<li>Arms<li>Waist<li>Legs<li>Charm</ul> | Yes
Base Defence                 | The defence score of the piece without any upgrades      | Yes

**NOTE**: Only two skills are supported per equipment piece.

**NOTE**: Charms do not require filling out the decoration slot or base defence columns.

#### JSON Configuration

A JSON configuration is required to instruct the application on how to score the equipment
combinations. The JSON file should look something like:

```json
{
  "decorations": {
    "deco_1": 1.0,
    "deco_2": 1.0,
    "deco_3": 1.0,
    "deco_4": 1.0,
    "num_decos": 1.0
  },
  "skills": {
    "Attack Boost": {
      "max": 7,
      "weight": 1.0,
      "penalty": 0.0
    },
    "Critical Eye": {
      "max": 7,
      "weight": 1.0,
      "penalty": 0.0
    },
    "Critical Boost": {
      "max": 3,
      "weight": 1.0,
      "penalty": 0.0
    }
  },
  "defence": 0.01,
  "limit": 100
}
```

Most of the attributes in the file specify the weight that the particular attribute should have in
a combination's score, which is the result of a linear combination of values using these weights.
The file is split into the following parts:

##### Decorations

Each line in this section defines a weight.

*   `deco_1` through `deco_4` describe the weight assigned to the number of decorations available in
    a combination at each respective decoration slot level.
*   `num_decos` defines the weight assigned to the total number of decorations present in a
    combination.

##### Skills

This section is split subsections, each involving a single skill. The subsection keys are the skill
names. Each subsection consists of:

*   A `max` attribute, which is the maximum level that skill can reach
*   A `weight` attribute, which is the weight assigned to that skill
*   A `penalty` attribute, which is the weight assigned to the skill if its levels exceeds the value
    defined for `max`.

##### Miscellaneous

Other attributes are:

*   The `defence` attribute which is the weight assigned to the amount of defence provided by the
    equipment piece
    *   **NOTE**: It is recommended to use a weight on the order of 0.01 given that defence values
        can soar to the hundreds
*   The `limit` attribute which defines the maximum number of combinations to output
