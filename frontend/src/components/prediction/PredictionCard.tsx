import Card from "../ui/Card";
import Badge from "../ui/Badge";

interface PredictionCardProps {
  title: string;
  metricName: string;
  value: string | number;
  confidence: number;
}

export function PredictionCard({ title, metricName, value, confidence }: PredictionCardProps) {
  return (
    <Card hoverable>
      <div className="flex justify-between items-start">
        <div>
          <p className="text-xs text-gray-400 uppercase tracking-wider">{title}</p>
          <p className="text-2xl font-bold mt-1 text-white">{value}</p>
        </div>
        <Badge variant={confidence > 0.8 ? "success" : "warning"}>
          {Math.round(confidence * 100)}% Confidence
        </Badge>
      </div>
      <div className="mt-4 flex items-center justify-between text-xs text-gray-400">
        <span>Metric: {metricName}</span>
        <span>GNN Prediction</span>
      </div>
    </Card>
  );
}
export default PredictionCard;
