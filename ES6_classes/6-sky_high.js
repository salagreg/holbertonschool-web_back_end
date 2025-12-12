import Building from './5-building.js';

export default class SkyHigh extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  removalWarningMessage() {
    return 'SkyHigh cannot be removed';
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
