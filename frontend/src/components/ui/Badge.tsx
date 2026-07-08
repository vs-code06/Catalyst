import React from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant?: "primary" | "secondary" | "success" | "warning" | "danger";
}

export function Badge({ className, variant = "primary", children, ...props }: BadgeProps) {
  return (
    <span
      className={twMerge(
        clsx(
          "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
          {
            "bg-catalyst-500/10 text-catalyst-400 border border-catalyst-500/20": variant === "primary",
            "bg-surface-tertiary text-gray-300 border border-surface-border": variant === "secondary",
            "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20": variant === "success",
            "bg-amber-500/10 text-amber-400 border border-amber-500/20": variant === "warning",
            "bg-rose-500/10 text-rose-400 border border-rose-500/20": variant === "danger",
          }
        ),
        className
      )}
      {...props}
    >
      {children}
    </span>
  );
}

export default Badge;

