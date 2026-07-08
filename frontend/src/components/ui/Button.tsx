import React from "react";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = "primary", size = "md", isLoading, children, ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={twMerge(
          clsx(
            "inline-flex items-center justify-center rounded-lg font-medium transition-all focus:outline-none focus:ring-2 focus:ring-catalyst-500 focus:ring-offset-2 focus:ring-offset-surface disabled:pointer-events-none disabled:opacity-50",
            {
              "bg-catalyst-600 text-white hover:bg-catalyst-500 shadow-lg shadow-catalyst-600/20": variant === "primary",
              "bg-surface-secondary text-gray-200 border border-surface-border hover:bg-surface-tertiary hover:text-white": variant === "secondary",
              "bg-red-600 text-white hover:bg-red-500 shadow-lg shadow-red-600/20": variant === "danger",
              "bg-transparent text-gray-400 hover:bg-surface-secondary hover:text-white": variant === "ghost",
              "h-8 px-3 text-xs": size === "sm",
              "h-10 px-4 text-sm": size === "md",
              "h-12 px-6 text-base": size === "lg",
            },
            className
          )
        )}
        {...props}
      >
        {isLoading ? (
          <svg className="mr-2 h-4 w-4 animate-spin text-current" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
          </svg>
        ) : null}
        {children}
      </button>
    );
  }
);

Button.displayName = "Button";
export default Button;
