export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  
    if (this.constructor !== Building && this.removalWarningMessage === undefined) {
      throw new Error("La classe héritant de Building doit redéfinir removalWarningMessage");
    }
  }
  get sqft() {
    return this._sqft;
  }
  set sqft(value) {
    this._sqft = value;
  }
}
