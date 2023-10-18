class LegendItem {
  title: string;
  color: string;
  isFor: any;
  textColor?: null | undefined;
  constructor(title: string, color: string, isFor: any , textColor: null | undefined) {
    this.title = title;
    this.color = color;
    this.isFor = isFor;
    this.textColor = textColor != null ? textColor : textColor;
  }
}

export default LegendItem;

