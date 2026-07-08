import React from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  hoverable?: boolean;
}

export function Card({ className, hoverable = false, children, ...props }: CardProps) {
  return (
    <div
      className={twMerge(
        clsx(
          "bg-surface-secondary border border-surface-border rounded-xl p-6 transition-all duration-200",
          {
            "hover:border-catalyst-500/50 hover:shadow-lg hover:shadow-catalyst-500/5": hoverable,
          }
        ),
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
}

export default Card;
