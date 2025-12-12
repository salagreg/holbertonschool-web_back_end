import Building from './5-building.js';

export default class SkyHigh extends Building {
  constructor(sqft, floors) {
    super(sqft, 100);
    this._floors = floors;
    this._sqft = sqft;
  }
  get floors() {
    return this._floors;
  }
  get sqft() {
    return this._sqft;
  }
  removalWarningMessage() {
    return 'SkyHigh buildings cannot be removed';
  }
  evacuationWarningMessage() {
    return `Evacuate the building immediately. There are ${this._floors} floors!`;
  }
}
