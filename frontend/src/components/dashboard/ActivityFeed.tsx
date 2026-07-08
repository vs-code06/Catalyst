export function ActivityFeed() {
  const items = [
    { id: 1, message: "Parsed catalyst-backend repository", time: "2 hours ago" },
    { id: 2, message: "Generated 3 simulation reports", time: "1 day ago" },
  ];

  return (
    <div className="space-y-4">
      <h3 className="text-lg font-medium text-white">Recent Activities</h3>
      <div className="flow-root">
        <ul className="-mb-8">
          {items.map((item, idx) => (
            <li key={item.id}>
              <div className="relative pb-8">
                {idx !== items.length - 1 && (
                  <span className="absolute top-4 left-4 -ml-px h-full w-0.5 bg-surface-border" aria-hidden="true" />
                )}
                <div className="relative flex space-x-3">
                  <div>
                    <span className="h-8 w-8 rounded-full bg-catalyst-500/10 border border-catalyst-500/20 flex items-center justify-center text-catalyst-400 text-xs">
                      🧬
                    </span>
                  </div>
                  <div className="flex-1 min-w-0 pt-1.5 flex justify-between space-x-4">
                    <div>
                      <p className="text-sm text-gray-300">{item.message}</p>
                    </div>
                    <div className="text-right text-xs whitespace-nowrap text-gray-400">
                      <time>{item.time}</time>
                    </div>
                  </div>
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
export default ActivityFeed;
