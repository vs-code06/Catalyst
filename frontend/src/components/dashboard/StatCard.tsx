import Card from "../ui/Card";

interface StatCardProps {
  label: string;
  value: string | number;
  change?: string;
  changeType?: "positive" | "negative" | "neutral";
}

export function StatCard({ label, value, change, changeType }: StatCardProps) {
  return (
    <Card>
      <p className="text-sm font-medium text-gray-400">{label}</p>
      <p className="text-3xl font-semibold mt-2 text-white">{value}</p>
      {change && (
        <span className={`text-xs mt-1 inline-block ${
          changeType === "positive" ? "text-emerald-400" :
          changeType === "negative" ? "text-rose-400" : "text-gray-400"
        }`}>
          {change}
        </span>
      )}
    </Card>
  );
}
export default StatCard;
