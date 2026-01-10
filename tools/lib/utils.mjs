/**
 * Utility functions for programmatic page generation
 */

import { mkdirSync, existsSync, rmSync } from 'fs';
import { dirname } from 'path';

/**
 * Generate cartesian product of input arrays
 * @param {Object} inputGrid - Object with arrays of values
 * @returns {Array} Array of all combinations
 */
export function cartesianProduct(inputGrid) {
  const keys = Object.keys(inputGrid);
  if (keys.length === 0) return [{}];

  const result = [];

  function generate(index, current) {
    if (index === keys.length) {
      result.push({ ...current });
      return;
    }

    const key = keys[index];
    const values = inputGrid[key];

    for (const value of values) {
      current[key] = value;
      generate(index + 1, current);
    }
  }

  generate(0, {});
  return result;
}

/**
 * Ensure directory exists
 * @param {string} filePath - Path to file (directory will be created)
 */
export function ensureDir(filePath) {
  const dir = dirname(filePath);
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
}

/**
 * Clean directory
 * @param {string} dirPath - Directory to clean
 */
export function cleanDir(dirPath) {
  if (existsSync(dirPath)) {
    rmSync(dirPath, { recursive: true, force: true });
  }
  mkdirSync(dirPath, { recursive: true });
}

/**
 * Format currency
 * @param {number} amount - Amount to format
 * @param {boolean} showCents - Whether to show cents
 * @returns {string} Formatted currency string
 */
export function formatCurrency(amount, showCents = false) {
  if (showCents) {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  }
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(amount);
}

/**
 * Format number with commas
 * @param {number} num - Number to format
 * @returns {string} Formatted number
 */
export function formatNumber(num) {
  return new Intl.NumberFormat('en-US').format(num);
}

/**
 * Format percentage
 * @param {number} pct - Percentage value
 * @param {number} decimals - Decimal places
 * @returns {string} Formatted percentage
 */
export function formatPercent(pct, decimals = 1) {
  return `${pct.toFixed(decimals)}%`;
}

/**
 * Slugify a string
 * @param {string} str - String to slugify
 * @returns {string} URL-safe slug
 */
export function slugify(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/**
 * Generate a hash for deduplication
 * @param {string} str - String to hash
 * @returns {string} Simple hash string
 */
export function simpleHash(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return Math.abs(hash).toString(36);
}

/**
 * Escape HTML entities
 * @param {string} str - String to escape
 * @returns {string} Escaped string
 */
export function escapeHtml(str) {
  const entities = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  };
  return String(str).replace(/[&<>"']/g, char => entities[char]);
}

/**
 * Parse command line arguments
 * @param {Array} args - Process argv
 * @returns {Object} Parsed arguments
 */
export function parseArgs(args) {
  const result = {
    flags: {},
    values: {}
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      const next = args[i + 1];

      if (next && !next.startsWith('-')) {
        result.values[key] = next;
        i++;
      } else {
        result.flags[key] = true;
      }
    } else if (arg.startsWith('-')) {
      result.flags[arg.slice(1)] = true;
    }
  }

  return result;
}

/**
 * Get site URL from environment or default
 * @returns {string} Site URL
 */
export function getSiteUrl() {
  return process.env.SITE_URL || 'https://plasmapaycalculator.com';
}

/**
 * Get current year
 * @returns {number} Current year
 */
export function getCurrentYear() {
  return new Date().getFullYear();
}

/**
 * Get current date in ISO format
 * @returns {string} ISO date string
 */
export function getISODate() {
  return new Date().toISOString().split('T')[0];
}

/**
 * Truncate text to specified length
 * @param {string} text - Text to truncate
 * @param {number} maxLength - Maximum length
 * @returns {string} Truncated text
 */
export function truncate(text, maxLength = 160) {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength - 3) + '...';
}

/**
 * Generate breadcrumb items
 * @param {Array} items - Array of { label, url } objects
 * @returns {Array} Breadcrumb items with home prepended
 */
export function generateBreadcrumbs(items) {
  return [
    { label: 'Home', url: '/' },
    ...items
  ];
}

/**
 * Console logging utilities
 */
export const log = {
  info: (msg) => console.log(`\x1b[36m[INFO]\x1b[0m ${msg}`),
  success: (msg) => console.log(`\x1b[32m[OK]\x1b[0m ${msg}`),
  warn: (msg) => console.log(`\x1b[33m[WARN]\x1b[0m ${msg}`),
  error: (msg) => console.log(`\x1b[31m[ERROR]\x1b[0m ${msg}`),
  dim: (msg) => console.log(`\x1b[90m${msg}\x1b[0m`)
};
