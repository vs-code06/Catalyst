import Button from "../ui/Button";

interface GraphControlsProps {
  onSearch: (query: string) => void;
  onFilterChange: (filters: any) => void;
  onReset: () => void;
}

export function GraphControls({ onSearch, onFilterChange: _onFilterChange, onReset }: GraphControlsProps) {
  return (
    <div className="flex flex-wrap gap-4 items-center justify-between p-4 bg-surface-secondary border border-surface-border rounded-xl">
      <div className="flex gap-2">
        <input
          type="text"
          placeholder="Search symbols..."
          className="bg-surface border border-surface-border px-3 py-1.5 rounded-lg text-sm text-white focus:outline-none focus:ring-1 focus:ring-catalyst-500"
          onChange={(e) => onSearch(e.target.value)}
        />
        <Button variant="secondary" size="sm" onClick={onReset}>
          Reset View
        </Button>
      </div>
    </div>
  );
}
export default GraphControls;
