# Zombie Implementation Guide by Chapter

This document lists all required zombies for the project, grouped by the five core chapters: **All Chapters** (core zombies), **Ancient Egypt**, **Frostbite Caves**, **Big Wave Beach**, and **Dark Ages**. Each entry includes the zombie’s alias (as found in `zombie properties.json`) and a brief explanation of its unique behavior.

---

## All Chapters (Core Zombies)

Basic zombies, armored variants, and the Gargantuar+Imp duo appear across multiple worlds.

| Alias | Explanation |
|-------|-------------|
| `ZombieTutorialDefault` | Basic zombie; moves and eats plants. |
| `ZombieTutorialArmor1Default` | Conehead zombie; has a cone armor that absorbs damage before health is affected. |
| `ZombieTutorialArmor2Default` | Buckethead zombie; stronger armor than Conehead. |
| `ZombieTutorialArmor4Default` | Brickhead zombie; even tougher armor. |
| `ZombieGargantuarBasic` | Huge zombie; smashes plants instantly and throws an Imp when damaged or near the house. |
| `ZombieTutorialImpDefault` | Small, fast zombie thrown by Gargantuar; runs after landing. |
| `ZombieTutorialFlagDefault` | Flag zombie; same as basic but used to mark wave starts. |

---

## Ancient Egypt

| Alias | Explanation |
|-------|-------------|
| `ZombieMummyDefault` | Basic Egyptian zombie. |
| `ZombieMummyArmor1Default` | Conehead Egyptian zombie. |
| `ZombieMummyArmor2Default` | Buckethead Egyptian zombie. |
| `ZombieMummyArmor4Default` | Brickhead Egyptian zombie. |
| `ZombiePharaohDefault` | Walks slowly inside a sarcophagus; after it breaks, the zombie runs faster. |
| `ZombieRaDefault` | Steals sun from the player’s reserve. |
| `ZombieExplorerDefault` | Carries a torch that instantly destroys specific plants (e.g., Frost Bonnet). |
| `ZombieTombRaiserDefault` | Summons graves (tombs) on the lawn. |
| `ZombieCamelDefault` | Three-segment camel zombie; only the front segment eats, rear segments follow. |
| `ZombieEgyptGargantuar` | Egyptian Gargantuar; smashes plants and throws an Egyptian Imp. |
| `ZombieEgyptImpDefault` | Imp thrown by Egyptian Gargantuar. |

---

## Frostbite Caves

| Alias                        | Explanation                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------- |
| `ZombieIceageDefault`        | Basic ice-age zombie.                                                        |
| `ZombieIceageArmor1Default`  | Conehead ice-age zombie.                                                     |
| `ZombieIceageArmor2Default`  | Buckethead ice-age zombie.                                                   |
| `ZombieIceageArmor3Default`  | Wears an ice block as armor; the block also chills plants that attack it.    |
| `ZombieIceAgeHunter`         | Ranged zombie; throws snowballs that chill or freeze plants from a distance. |
| `ZombieIceAgeTroglobite`     | Pushes ice blocks down the lane; blocks crush plants and absorb damage.      |
| `ZombieIceAgeDodo`           | Flies over certain plants and obstacles.                                     |
| `ZombieWeaselHoarderDefault` | When damaged, releases fast, weak weasels (similar to chickens).             |
| `ZombieWeaselDefault`        | The small, fast weasel unit.                                                 |
| `ZombieIceAgeGargantuar`     | Gargantuar of Frostbite Caves; throws an ice-age Imp.                        |
| `ZombieIceageImpDefault`     | Imp thrown by ice-age Gargantuar.                                            |

---

## Big Wave Beach

| Alias | Explanation |
|-------|-------------|
| `ZombieBeachDefault` | Basic beach zombie. |
| `ZombieBeachArmor1Default` | Conehead beach zombie. |
| `ZombieBeachArmor2Default` | Buckethead beach zombie. |
| `ZombieBeachSnorkel` | Walks underwater; invulnerable to most plants except when surfacing to eat. |
| `ZombieBeachSurfer` | Rides a surfboard; moves very fast and crushes plants. After losing the board, becomes a normal zombie. |
| `ZombieBeachFisherman` | Casts a fishing line to hook plants and pull them toward himself. |
| `ZombieBeachOctopus` | Throws octopi that disable plants. |
| `ZombieBeachGargantuar` | Beach Gargantuar; throws a beach Imp. |
| `ZombieBeachImpDefault` | Imp thrown by beach Gargantuar. |
| `ZombieBeachFastSwimmer` | Swims quickly in water lanes but is slow on land. |

---

## Dark Ages

| Alias | Explanation |
|-------|-------------|
| `ZombieDarkDefault` | Basic Dark Ages zombie. |
| `ZombieDarkArmor1Default` | Conehead Dark Ages zombie. |
| `ZombieDarkArmor2Default` | Buckethead Dark Ages zombie. |
| `ZombieDarkArmor3Default` | Wears shoulder armor and a crown; higher durability. |
| `ZombieDarkArmor4Default` | Brickhead Dark Ages zombie. |
| `ZombieWizardDefault` | Casts a spell to transform plants into harmless sheep. |
| `ZombieDarkJugglerDefault` | Catches and reflects many projectiles back at plants. |
| `ZombieDarkKing` | Buffs nearby Dark Ages zombies (e.g., increases speed or damage). |
| `ZombieDarkGargantuar` | Dark Ages Gargantuar; throws a Dark Ages Imp. |
| `ZombieDarkImpDefault` | Imp thrown by Dark Ages Gargantuar. |

---

```json
{
      "aliases": [
        "ZombieMummyDefault"
      ],
      "objclass": "ZombiePropertySheet",
      "objdata": {
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 190,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 5,
          "y": 0,
          "z": 1.4
        },
        "Speed": 0.185,
        "WavePointCost": 100,
        "Weight": 1000,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness1"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
    {
      "aliases": [
        "ZombieMummyArmor1Default"
      ],
      "objclass": "ZombiePropertySheet",
      "objdata": {
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 190,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 0,
          "y": 0,
          "z": 1.2
        },
        "Speed": 0.185,
        "WavePointCost": 200,
        "Weight": 3000,
        "ZombieArmorProps": [
          "RTID(ConeDefault@ArmorTypes)"
        ],
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness3"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
    {
      "aliases": [
        "ZombieMummyArmor2Default"
      ],
      "objclass": "ZombiePropertySheet",
      "objdata": {
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 190,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 0,
          "y": 0,
          "z": 1.2
        },
        "Speed": 0.185,
        "WavePointCost": 400,
        "Weight": 4000,
        "ZombieArmorProps": [
          "RTID(BucketDefault@ArmorTypes)"
        ],
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness5"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
    {
      "aliases": [
        "ZombieMummyArmor4Default"
      ],
      "objclass": "ZombiePropertySheet",
      "objdata": {
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 190,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 0,
          "y": 0,
          "z": 1.2
        },
        "Speed": 0.185,
        "WavePointCost": 700,
        "Weight": 3000,
        "ZombieArmorProps": [
          "RTID(BrickDefault@ArmorTypes)"
        ],
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness6"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
```

```json
{
      "objclass": "ArmorPropertySheet",
      "aliases": [
        "ConeDefault"
      ],
      "objdata": {
        "ArmorType": "Cone",
        "BaseHealth": 370,
        "ArmorFlags": [
          "damageable",
          "droppable",
          "helm"
        ],
        "ArmorLayers": [
          "zombie_armor_cone_norm",
          "zombie_armor_cone_damage_01",
          "zombie_armor_cone_damage_02"
        ],
        "ArmorLayerHealth": [
          0.666,
          0.333
        ],
        "ImpactSoundEvent": "Play_impact_plastic"
      }
    },
    {
      "objclass": "ArmorPropertySheet",
      "aliases": [
        "BucketDefault"
      ],
      "objdata": {
        "ArmorType": "Bucket",
        "BaseHealth": 1100,
        "ArmorFlags": [
          "metallic",
          "damageable",
          "droppable",
          "helm"
        ],
        "ArmorLayers": [
          "zombie_armor_bucket_norm",
          "zombie_armor_bucket_damage_01",
          "zombie_armor_bucket_damage_02"
        ],
        "ArmorLayerHealth": [
          0.666,
          0.333
        ],
        "ImpactSoundEvent": "Play_impact_shieldhit"
      }
    },
    {
      "objclass": "ArmorPropertySheet",
      "aliases": [
        "BrickDefault"
      ],
      "objdata": {
        "ArmorType": "Brick",
        "BaseHealth": 2200,
        "ArmorFlags": [
          "damageable",
          "droppable",
          "helm"
        ],
        "ArmorLayers": [
          "zombie_armor_brick_norm",
          "zombie_armor_brick_damage_01",
          "zombie_armor_brick_damage_02"
        ],
        "ArmorLayerHealth": [
          0.666,
          0.333
        ],
        "ParticleLayerOverride": [
          "zombie_armor_brick_damage_02",
          "zombie_armor_brick_damage_02",
          "zombie_armor_brick_damage_02"
        ]
      }
    },
```

```json
{
      "aliases": [
        "ZombieEgyptGargantuar"
      ],
      "objclass": "ZombieGargantuarProps",
      "objdata": {
        "AlmanacOffset": {
          "x": -10,
          "y": 40
        },
        "AlmanacScale": 1,
        "ArmDropFraction": -1,
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 30,
          "mX": 0,
          "mY": 10
        },
        "CanBeFlickedOff": false,
        "CanSpawnPlantFood": false,
        "Cost": 150,
        "EatDPS": 0,
        "ExplodesWhenMowed": true,
        "FlickIsLaneRestricted": true,
        "GroundTrackName": "ground_swatch",
        "HealthThresholdToImpAmmoLayers": [
          {
            "HealthPercentThrowImp": 0.5,
            "ProjectileLayersToHide": [
              "zombie_imp_skull",
              "zombie_imp_jaw",
              "Zombie_gargantuar_whiterope",
              "zombie_imp_arm_inner_lower",
              "zombie_imp_arm_inner_upper",
              "zombie_imp_arm_outer_lower",
              "zombie_imp_arm_outer_upper_01",
              "zombie_imp_arm_outer_upper_02",
              "zombie_imp_arms_outer_upper",
              "zombie_imp_eye",
              "zombie_imp_eye_sm",
              "zombie_imp_hand_inner",
              "zombie_imp_hand_outer",
              "zombie_imp_leg_inner_lower",
              "zombie_imp_leg_inner_upper",
              "zombie_imp_leg_outer_lower",
              "zombie_imp_leg_outer_upper",
              "zombie_imp_pupil",
              "zombie_imp_torso",
              "zombie_imp_waist",
              "zombie_imp_toe_outer",
              "zombie_imp_toe_inner"
            ]
          }
        ],
        "HitRect": {
          "mHeight": 95,
          "mWidth": 62,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 3600,
        "HypnoshroomEffectOffset": {
          "x": 0,
          "y": 120
        },
        "ImpApex": 250,
        "ImpFlightTime": 1.5,
        "ImpSpawnOffset": {
          "x": -100,
          "y": 2,
          "z": 115
        },
        "ImpTargetColumn": 2,
        "ImpType": "egypt_imp",
        "IsValidPinchTarget": false,
        "MinPosXThrowImp": 400,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "SmashDamage"
          }
        ],
        "ShadowOffset": {
          "x": 5,
          "y": 0,
          "z": 1.4
        },
        "Size": "large",
        "SkipHeadDropState": true,
        "SmashDamage": 1500,
        "SmashDuration": 2,
        "SoundOnAsh": "Play_Zomb_Global_Gargantuar_Mvmt_Death_Ash",
        "SoundOnElectrocute": "Play_Zomb_Global_Gargantuar_Mvmt_Shock",
        "SoundOnIdle": "Play_Zomb_Egypt_Gargantuar_Mvmt_Idle",
        "Speed": 0.24,
        "StaticArtImageAsset": "IMAGE_GARGANTUAR",
        "ThrowImpDuration": 1,
        "WavePointCost": 1500,
        "Weight": 3000,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness7"
          },
          {
            "Type": "speed",
            "Value": "speed3"
          }
        ]
      }
    },
```

```json
{
      "aliases": [
        "ZombieEgyptImpDefault"
      ],
      "objclass": "ZombiePropertySheet",
      "objdata": {
        "ArtCenter": {
          "x": 102,
          "y": 124
        },
        "AttackRect": {
          "mHeight": 80,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": false,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 80,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 190,
        "HypnoshroomEffectOffset": {
          "x": -6,
          "y": 36
        },
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 5,
          "y": 0,
          "z": 0.8
        },
        "Size": "imp",
        "Speed": 0.22,
        "WavePointCost": 100,
        "Weight": 1000,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness1"
          },
          {
            "Type": "speed",
            "Value": "speed3"
          }
        ]
      }
    },
```

```json
{
      "aliases": [
        "ZombieRaDefault"
      ],
      "objclass": "ZombieRaProps",
      "objdata": {
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 190,
        "MaxClaimedSunCurrency": 250,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 10,
          "y": 0,
          "z": 1.2
        },
        "Speed": 0.2,
        "WavePointCost": 100,
        "Weight": 700,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness1"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
```

```json
{
      "aliases": [
        "ZombieExplorerDefault"
      ],
      "objclass": "ZombieExplorerProps",
      "objdata": {
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 0,
          "mY": 10
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 5,
          "mY": 10
        },
        "Hitpoints": 250,
        "MaxTorchReach": 37,
        "PlantsToEat": {
          "List": [
            "frostbonnet",
            "blazingknight"
          ],
          "ListType": "includelist"
        },
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 5,
          "y": 0,
          "z": 1.4
        },
        "Speed": 0.25,
        "WavePointCost": 250,
        "Weight": 3000,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness2"
          },
          {
            "Type": "speed",
            "Value": "speed3"
          }
        ]
      }
    },
```

```json
{
      "aliases": [
        "ZombieTombRaiserDefault"
      ],
      "objclass": "ZombieTombRaiserProps",
      "objdata": {
        "# TombRaiser specific properties ": 0,
        "Ammo": 5,
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 380,
        "NumberOfTombsToSpawn": 2,
        "Projectile": "RTID(ZombieBoneDefault@ProjectileTypes)",
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 10,
          "y": 0,
          "z": 1.2
        },
        "Speed": 0.185,
        "TimeBetweenCasts": 0,
        "TimeBetweenRaisings": 6,
        "WavePointCost": 300,
        "Weight": 2000,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness4"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
```

```json
{
      "aliases": [
        "ZombieIceAgeDodo"
      ],
      "objclass": "ZombieIceAgeDodoProps",
      "objdata": {
        "AddRandomChanceForJumpPerGridWalked": 0.1,
        "ArmDropFraction": -1,
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 35,
          "mX": 5,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "ChillInsteadOfFreeze": true,
        "CooldownSecondsUntilNextJumpAvailable": 0,
        "Cost": 150,
        "EatDPS": 100,
        "ElectrocutePAMName": "POPANIM_EFFECTS_ZOMBIE_DODO_SHOCK",
        "GridItemsToFlyOver": {
          "List": [
            "slider_down",
            "slider_up",
            "slider_down_modern",
            "slider_up_modern",
            "lava",
            "shallowpuddle",
            "potholepuddle"
          ],
          "ListType": "includelist"
        },
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 46,
          "mX": 7,
          "mY": 10
        },
        "Hitpoints": 490,
        "InitialSetRandomChanceForJump": 0,
        "LandedResetRandomChanceForJump": 0.35,
        "MaxRandomGridSquaresToFlyOver": 2,
        "MaximumGridSquaresToFlyOver": 2,
        "MinRandomGridSquaresToFlyOver": 1,
        "PlantsToFlyOver": {
          "List": [
            "spikeweed",
            "spikerock",
            "iceburg",
            "wallnut",
            "potatomine",
            "lavaguava",
            "endurian",
            "cactus",
            "primalwallnut",
            "primalpotatomine",
            "escaperoot",
            "murkadamia",
            "tombtangler",
            "vamporcini"
          ],
          "ListType": "includelist"
        },
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 10,
          "y": 0,
          "z": 1.2
        },
        "SkipHeadDropState": true,
        "Speed": 0.3,
        "WavePointCost": 600,
        "Weight": 3500,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness3"
          },
          {
            "Type": "speed",
            "Value": "speed4"
          }
        ]
      }
    },
```

```json

      "aliases": [
        "ZombieIceAgeHunter"
      ],
      "objclass": "ZombieIceAgeHunterProps",
      "objdata": {
        "Actions": [
          "RTID(ZombieIceAgeProjectileAction@ZombieActions)"
        ],
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "ChillInsteadOfFreeze": true,
        "Cost": 150,
        "EatDPS": 100,
        "FarAttackRange": 4,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 700,
        "NearAttackRange": 1,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 10,
          "y": 0,
          "z": 1.2
        },
        "SnowballsPerBarrage": 3,
        "Speed": 0.12,
        "WavePointCost": 500,
        "Weight": 3500,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness4"
          },
          {
            "Type": "speed",
            "Value": "speed0"
          }
        ]
      }
    },
```

```json
 {
      "aliases": [
        "ZombieIceAgeTroglobite"
      ],
      "objclass": "ZombieIceAgeTroglobiteProps",
      "objdata": {
        "Actions": [
          "RTID(ZombiePushGridItemAction@ZombieActions)"
        ],
        "ArtCenter": {
          "x": 90,
          "y": 125
        },
        "AttackRect": {
          "mHeight": 95,
          "mWidth": 20,
          "mX": 15,
          "mY": 0
        },
        "CanSpawnPlantFood": true,
        "ChillInsteadOfFreeze": true,
        "Cost": 150,
        "EatDPS": 100,
        "GroundTrackName": "ground_swatch",
        "HitRect": {
          "mHeight": 95,
          "mWidth": 32,
          "mX": 10,
          "mY": 10
        },
        "Hitpoints": 470,
        "ImpType": "iceage_imp",
        "NumberOfIceblocksToSpawnWith": 3,
        "ScaledProps": [
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "Hitpoints"
          },
          {
            "Arg1": 1.3,
            "Arg2": 0.05,
            "Formula": "standard",
            "Key": "EatDPS"
          },
          {
            "Formula": "constant",
            "Key": "Speed"
          },
          {
            "Formula": "constant",
            "Key": "WavePointCost"
          }
        ],
        "ShadowOffset": {
          "x": 10,
          "y": 0,
          "z": 1.2
        },
        "Speed": 0.185,
        "WavePointCost": 600,
        "Weight": 3500,
        "ZombieStats": [
          {
            "Type": "toughness",
            "Value": "toughness4"
          },
          {
            "Type": "speed",
            "Value": "speed2"
          }
        ]
      }
    },
```