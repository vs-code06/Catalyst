import React, { useState } from "react";

export interface TooltipProps {
  content: string;
  children: React.ReactElement;
}

export function Tooltip({ content, children }: TooltipProps) {
  const [show, setShow] = useState(false);

  return (
    <div className="relative inline-block" onMouseEnter={() => setShow(true)} onMouseLeave={() => setShow(false)}>
      {children}
      {show && (
        <div className="absolute z-50 bottom-full left-1/2 -translate-x-1/2 mb-2 w-max max-w-xs rounded bg-surface-tertiary px-2 py-1 text-xs text-white shadow-md border border-surface-border">
          {content}
        </div>
      )}
    </div>
  );
}
