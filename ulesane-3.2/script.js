var nameList = [
  "Time",
  "Past",
  "Future",
  "Dev",
  "Fly",
  "Flying",
  "Soar",
  "Soaring",
  "Power",
  "Falling",
  "Fall",
  "Jump",
  "Cliff",
  "Mountain",
  "Rend",
  "Red",
  "Blue",
  "Green",
  "Yellow",
  "Gold",
  "Demon",
  "Demonic",
  "Panda",
  "Cat",
  "Kitty",
  "Kitten",
  "Zero",
  "Memory",
  "Trooper",
  "XX",
  "Bandit",
  "Fear",
  "Light",
  "Glow",
  "Tread",
  "Deep",
  "Deeper",
  "Deepest",
  "Mine",
  "Your",
  "Worst",
  "Enemy",
  "Hostile",
  "Force",
  "Video",
  "Game",
  "Donkey",
  "Mule",
  "Colt",
  "Cult",
  "Cultist",
  "Magnum",
  "Gun",
  "Assault",
  "Recon",
  "Trap",
  "Trapper",
  "Redeem",
  "Code",
  "Script",
  "Writer",
  "Near",
  "Close",
  "Open",
  "Cube",
  "Circle",
  "Geo",
  "Genome",
  "Germ",
  "Spaz",
  "Shot",
  "Echo",
  "Beta",
  "Alpha",
  "Gamma",
  "Omega",
  "Seal",
  "Squid",
  "Money",
  "Cash",
  "Lord",
  "King",
  "Duke",
  "Rest",
  "Fire",
  "Flame",
  "Morrow",
  "Break",
  "Breaker",
  "Numb",
  "Ice",
  "Cold",
  "Rotten",
  "Sick",
  "Sickly",
  "Janitor",
  "Camel",
  "Rooster",
  "Sand",
  "Desert",
  "Dessert",
  "Hurdle",
  "Racer",
  "Eraser",
  "Erase",
  "Big",
  "Small",
  "Short",
  "Tall",
  "Sith",
  "Bounty",
  "Hunter",
  "Cracked",
  "Broken",
  "Sad",
  "Happy",
  "Joy",
  "Joyful",
  "Crimson",
  "Destiny",
  "Deceit",
  "Lies",
  "Lie",
  "Honest",
  "Destined",
  "Bloxxer",
  "Hawk",
  "Eagle",
  "Hawker",
  "Walker",
  "Zombie",
  "Sarge",
  "Capt",
  "Captain",
  "Punch",
  "One",
  "Two",
  "Uno",
  "Slice",
  "Slash",
  "Melt",
  "Melted",
  "Melting",
  "Fell",
  "Wolf",
  "Hound",
  "Legacy",
  "Sharp",
  "Dead",
  "Mew",
  "Chuckle",
  "Bubba",
  "Bubble",
  "Sandwich",
  "Smasher",
  "Extreme",
  "Multi",
  "Universe",
  "Ultimate",
  "Death",
  "Ready",
  "Monkey",
  "Elevator",
  "Wrench",
  "Grease",
  "Head",
  "Theme",
  "Grand",
  "Cool",
  "Kid",
  "Boy",
  "Girl",
  "Vortex",
  "Paradox",
];

class Platform {
  constructor(resources) {
    this.resources = resources;
  }
  consume(amount) {
    this.resources -= amount;
  }
}

class Floor {
  constructor(lvl, peopleList) {
    this.lvl = lvl;
    this.peopleList = peopleList;
  }
  process_platform(platform) {
    console.log("korrus", this.lvl);
    this.peopleCount.forEach((person) => {
      person.makeDecision(platform);
    });
    console.log("resurside jääk: ", platform.resources);
  }
}

class Person {
  constructor(name, percent) {
    this.name = name;
    this.percent = percent;
  }

  makeDecision(platform) {
    let chance = Math.random() * 100;
    if (chance <= this.percent && platform.resources > 0) {
      const eatAmount = 10;
      platform.consume(eatAmount);
      console.log(this.name, "sõid ", eatAmount, "toitu");
    }
  }
}

let floors = [];
for (let i = 0; i < 10; i++) {
  let person1 = new Person(
    nameList[Math.floor(Math.random() * nameList.length)],
    Math.floor(Math.random() * 100) + 1
  );
  let person2 = new Person(
    nameList[Math.floor(Math.random() * nameList.length)],
    Math.floor(Math.random() * 100) + 1
  );
  let floor = new Floor(i, [person1, person2]);
  floors.push(floor);
}

console.log(floors);

let platform = new Platform(100);
console.log(platform);

floors.forEach((floor) => {
  floor.process_platform(platform);
});
